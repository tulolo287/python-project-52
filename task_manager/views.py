from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.urls import (
    reverse_lazy,
)
from django.contrib import (
    messages,
)


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("home")

    def form_valid(
        self,
        form,
    ):
        messages.info(
            self.request,
            "Login successfully",
        )
        return super().form_valid(form)

    def form_invalid(
        self,
        form,
    ):
        messages.error(
            self.request,
            "Login Error",
        )
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")
    success_message = "You have been logged out."

    def dispatch(
        self,
        request,
        *args,
        **kwargs,
    ):
        # messages.info(request, 'You have been logged out.'
        return super().dispatch(
            request,
            *args,
            **kwargs,
        )
