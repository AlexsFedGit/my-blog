from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class AppLoginView(LoginView):
    template_name = 'accounts/login.html'


class AppLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'
