from django.db import models


class UserProfile(models.Model):
    github = models.CharField(max_length=120)
    first_name = models.CharField(max_length=80)
    second_name = models.CharField(max_length=120)
    role = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
