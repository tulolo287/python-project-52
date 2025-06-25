from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from task_manager.users.forms import UserCreateForm
from task_manager.users.mixins import (
    ProtectDeleteMixin,
    CheckChangePermissionMixin,
    CustomLoginRequiredMixin,
)
from task_manager.users.models import User


class UserIndexView(ListView):
    model = User
    context_object_name = "users"
    template_name = "users/index.html"
    extra_context = {
        'title': translate('Users'),
        'ID': translate('ID'),
        'username': translate('Username'),
        'full_name': translate('Full name'),
        'edit': translate('Edit'),
        'delete': translate('Delete'),
        'created_at': translate('Created at'),
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = "form.html"
    success_url = reverse("login")
    extra_context = {
        'title': translate('Registration'),
        'submit': translate('Register'),
    }
    success_message = translate('User created successfully')


class UserUpdateView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserCreateForm
    template_name = "form.html"
    success_url = reverse("users")
    extra_context = {
        'title': translate('Edit user'),
        'submit': translate('Update'),
    }
    success_message = translate('User update successfully')


class UserDeleteView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    ProtectDeleteMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    context_object_name = "user"
    template_name = "users/delete.html"
    success_url = reverse("users")
    extra_context = {
        'title': translate('Remove user'),
        'submit': translate('Yes, remove'),
        'confirm': translate('Are you sure delete'),
    }
    success_message = translate('User was successfully deleted')
