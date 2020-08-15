from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from skills_parser.parser import RepoParser

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    role_choices = [
        ('Backend Developer', 'Backend Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('FullStack Developer', 'FullStack Developer'),
        ('Quality Assurance', 'Quality Assurance'),
        ('DB Administrator', 'DB Administrator'),
        ('DevOps', 'DevOps'),
        ('Data Analyst', 'Data Analyst'),
        ('Data Scientist', 'Data Scientist'),
        ('Big Data Engineer', 'Big Data Engineer'),
        ('Blockchain Developer', 'Blockchain Developer'),
        ('Software Architect', 'Software Architect'),
        ('Penetration Tester', 'Penetration Tester'),
        ('Security Engineer', 'Security Engineer'),
    ]

    github = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6'})
    )
    second_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6'})
    )
    role = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'dropdown'}),
        choices=role_choices,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control col-md-6'})
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}),
        validators=[
            RegexValidator(
                r'\+?[0-9]{7,15}',
                message="Phone number must contain only numbers and one plus"
            )
        ]
    )

    def clean_github(self):
        username = self.cleaned_data['github']
        if not RepoParser.check_user_exists(username):
            raise ValidationError(message="Github user doesn't exists")
        return username


    class Meta:
        model = UserProfile
        fields = '__all__'
