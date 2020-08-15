from typing import Dict

from django.conf import settings
from post_office import mail
from skills_parser.parser import RepoParser


def send_email(context: dict):
    mail.send(
        settings.EMAIL_ENTERPRISES,
        'FreshInterns <freshinternships@gmail.com>',
        subject='Internship candidates',
        message="""Dear Sir/Madam,
            I am writing to let you know that we have a new keen intern for you!
            Maybe you'll find that our candidate is a skilled developer.
            
            Short information about the applicant
            
            {{ first_name }} {{ second_name }}
            {{ role }}
            
            Contacts:
            {{ phone_number }}
            {{ email }}
            {{ github }}
            
            He has proven experience in these technologies:
            {{ skills }}
            
            Please contact with him/her if you are interested in that candidate!
            
            Kind regards,
            FreshInterns Co.
        """,
        context=context,
    )

def get_skill_set(self, username: str) -> Dict[str, int]:
    result: dict
    parser = RepoParser(username)
    parser.get_repos()
    return parser.get_skills_list()

def render_skill_list(skills: dict) -> str:
    result = ''
    for i, s in enumerate(skills.keys()):
        result += f'{i}. {s} - ' + str(skills[s]) + ' months;\n'
    return result

def make_context(cleaned_data: dict) -> dict:
    """Make message context.

    Collect all the available data together.
    """
    context = {}
    parser = RepoParser(cleaned_data['github'])
    parser.get_repos()
    skills = parser.get_skills_list()

    context['first_name'] = cleaned_data['first_name']
    context['second_name'] = cleaned_data['second_name']
    context['role'] = cleaned_data['role']
    context['email'] = cleaned_data['email']
    context['phone'] = cleaned_data['phone']
    context['github'] = 'https://github.com/' + cleaned_data['github']

    context['skills'] = render_skill_list(skills)
    return context
