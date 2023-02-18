from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from app import settings


class AppLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['next'] == reverse_lazy('accounts:logout'):
            context['next'] = settings.LOGIN_REDIRECT_URL
        return context


class AppLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'
