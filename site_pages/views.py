from django.urls import reverse
from django.views.generic.edit import CreateView

from .email import make_context, send_email
from .forms import UserProfileForm


class InternFormView(CreateView):
    template_name = 'resume.html'
    form_class = UserProfileForm

    def form_valid(self, form):
        context = make_context(form.cleaned_data)
        send_email(context)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
