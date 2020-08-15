from django.urls import reverse
from django.views.generic.edit import CreateView

from .email import make_context, send_email
from .forms import UserProfileForm


class InternFormView(CreateView):
    template_name = 'resume.html'
    form_class = UserProfileForm

    def get_success_url(self):
        context = make_context(self.cleaned_data)
        send_email(context)
        return reverse('index')
