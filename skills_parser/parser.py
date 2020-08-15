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


class UserParser(object):
    username: str
    repo_list: List[str]

    def __init__(self, username, *args, **kwargs):
        self.username = username
        if not self.check_user_exists():
            raise ValidationError(message="Github user doesn't exists")

    @classmethod
    def response_has_errors(cls, response: dict) -> bool:
        return response.get('message')

    def check_user_exists(self) -> bool:
        """Check that user with given name is registered on Github."""
        response = requests.get(
            'https://api.github.com/users/' + self.username
        ).json()
        # If there is no error message return True
        return not response.get('message', None)

    @classmethod
    def sort_repos_by(cls, field: str, repos: List[dict]):
        if repos[0].get(field) is None:
            return
        return sorted(repos, key=itemgetter(field), reverse=True)

    @classmethod
    def parse_repos(cls, response: Dict[str, str]) -> List[str]:
        """Parse retrieved user repo list."""
        raw = response.json()
        raw = __class__.sort_repos_by('size', raw)
        
        parsed: List[str] = []
        # Select 15 biggest repos
        # Needed in order to reduce the server load
        for repo in raw[:15]:
            parsed.append(repo['name'])
        return parsed

    def get_repos(self) -> List[str]:
        """Retrieve and parse user repo list."""
        # Get up to 100 latest repos
        response = requests.get(
            f'https://api.github.com/users/{self.username}/repos',
            params={
                'sort': 'pushed',
            }
        )
        self.repo_list = __class__.parse_repos(response)
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
