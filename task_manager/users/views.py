from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy as redirect
from task_manager.users.forms import UserCreateForm
from task_manager.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class UserIndexView(ListView):
    model = User
    context_object_name = "users"
    template_name = "users/index.html"


class UserCreateView(CreateView, SuccessMessageMixin):
    form_class = UserCreateForm
    template_name = "users/create.html"
    success_url = redirect("login")
    success_message = "User created successfully"


class UserUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = UserCreateForm
    template_name = "users/update.html"
    success_url = redirect("users")
    success_message = "User update successfully"


class UserDeleteView(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = User
    context_object_name = "users"
    template_name = "users/delete.html"
    success_url = redirect("users")
    success_message = "User delete successfully"
