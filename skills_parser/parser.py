from datetime import datetime
from operator import itemgetter
from typing import Dict, List

import requests
from django.core.exceptions import ValidationError


class Repository(object):
    # Defines age of repository in months
    age: int
    # Defines top 10 languages used in the project
    languages: List[str]
    # Repository name
    name: str

    def __init__(self, name, languages=[], age=0, *args, **kwargs):
        self.name = name
        self.languages = languages
        self.age = age


class RepoParser(object):
    username: str
    repo_list: List[Repository]

    def __init__(self, username, *args, **kwargs):
        self.username = username
        if not __class__.check_user_exists(username):
            raise ValidationError(message="Github user doesn't exists")

    @classmethod
    def response_has_errors(cls, response: dict) -> bool:
        return response.get('message')

    @classmethod
    def check_user_exists(cls, username: str) -> bool:
        """Check that user with given name is registered on Github."""
        response = requests.get(
            'https://api.github.com/users/' + username
        ).json()
        # If there is no error message return True
        return not response.get('message', None)

    @classmethod
    def sort_repos_by(cls, field: str, repos: List[dict]) -> List[dict]:
        if repos[0].get(field) is None:
            return
        return sorted(repos, key=itemgetter(field), reverse=True)

    @classmethod
    def get_repos_age(cls, response: List[dict]) -> Dict[str, int]:
        """Retrieve a list of repos age in months."""
        result = {}
        for repo in response:
            begin = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            end = datetime.strptime(repo['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")
            age = (end - begin).days // 30
            result[repo['name']] = age
        return result

    def parse_repos(self, response: Dict[str, str]) -> List[Repository]:
        """Parse retrieved user repo list.

        Returns list of Repository instances
        initialized by names.
        """
        raw = response.json()
        raw = __class__.sort_repos_by('size', raw)

        # Select 15 biggest repos
        # Needed in order to reduce the server load
        ages = __class__.get_repos_age(raw[:15])
        # Filter repositories which are at least one month old
        ages = {r: ages[r] for r in ages.keys() if ages[r] > 0}

        
        parsed = []
        for repo_name in ages.keys():
            # Get top languages from the project
            languages = self.get_top_languages(repo_name)
            new = Repository(
                repo_name, age=ages[repo_name], languages=languages
            )
            parsed.append(new)
        return parsed

    def get_repos(self) -> List[Repository]:
        """Retrieve and parse user repo list.

        Returns list of processed instances
        of Repository class.
        """
        # Get up to 100 latest repos
        response = requests.get(
            f'https://api.github.com/users/{self.username}/repos',
            params={
                'sort': 'pushed',
            }
        )
        self.repo_list = self.parse_repos(response)
        return self.repo_list

    def get_top_languages(self, repo_name: str) -> List[str]:
        response = requests.get(
            f'https://api.github.com/repos/{self.username}'
            f'/{repo_name}/languages'
        ).json()
        if __class__.response_has_errors(response):
            return []
        # Return top ten languages
        return list(response)[:10]

    def get_skills_list(self) -> Dict[str, int]:
        """Get list of skills in format: 'skill_name': month_of_experience.

        Needs to call after the get_repos method.
        """
        skills = {}
        for r in self.repo_list:
            for l in r.languages:
                if skills.get(l):
                    skills[l] += r.age
                else:
                    skills[l] = r.age
        return skills
