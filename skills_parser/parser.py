from operator import itemgetter
from typing import Dict, List

import requests
from django.core.exceptions import ValidationError


class UserParser(object):
    username: str
    repo_list: List[str]

    def __init__(self, username, *args, **kwargs):
        self.username = username
        if not self.check_user_exists():
            raise ValidationError(message="Github user doesn't exists")

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
    def parse_user_repos(cls, response: Dict[str, str]) -> List[str]:
        """Parse retrieved user repo list."""
        raw = response.json()
        raw = __class__.sort_repos_by('size', raw)
        
        parsed: List[str] = []
        # Select 15 biggest repos
        # Needed in order to reduce the server load
        for repo in raw[:15]:
            parsed.append(repo['name'])
        self.repo_list = parsed
        return parsed

    def get_user_repos(self) -> List[str]:
        """Retrieve and parse user repo list."""
        # Get up to 100 latest repos
        response = requests.get(
            'https://api.github.com/users/' +
            self.username +
            '/repos',
            params={
                'sort': 'pushed',
            }
        )
        return __class__.parse_user_repos(response)

    def get_top_languages(self) -> List[str]:
        pass
