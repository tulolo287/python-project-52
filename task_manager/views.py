from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        "title": translate("Task manager"),
    }


class LoginView(LoginView):
    template_name = "form.html"
    next_page = reverse("home")
    extra_context = {
        "title": translate("Login"),
        "submit": translate("Enter"),
    }

    def form_valid(self, form):
        messages.info(self.request, translate("Login successfully"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, translate("Login Error"))
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse("home")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, translate("Logged out successfully"))
        return super().dispatch(request, *args, **kwargs)
