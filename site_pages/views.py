from django.urls import reverse
from django.views.generic.edit import CreateView

from .forms import UserProfileForm


class InternFormView(CreateView):
    template_name = 'resume.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse('index')
