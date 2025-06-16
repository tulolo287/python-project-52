from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from task_manager.users.models import User
from .forms import TaskForm
from .mixins import AuthorRequireMixin
from .models import Task


class TaskIndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    extra_context = {
        'title': translate('Tasks'),
        'ID': translate('ID'),
        'name': translate('Name'),
        'status': translate('Status'),
        'author': translate('Author'),
        'executor': translate('Executor'),
        'edit': translate('Edit'),
        'delete': translate('Delete'),
        'select': translate('Select'),
        'created_at': translate('Created at'),
    }
    permission_denied_message = translate('Please login')


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse('tasks')
    extra_context = {
        'title': translate('Add Task'),
        'submit': translate('Create'),
    }
    success_message = translate('Task created successfully')
    permission_denied_message = translate('Please login')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse('tasks')
    extra_context = {
        'title': translate('Edit task'),
        'submit': translate('Update'),
    }
    success_message = translate('Task updated successfully')
    permission_denied_message = translate('Please login')


class TaskDeleteView(
    LoginRequiredMixin, AuthorRequireMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = 'tasks/delete.html'
    context_object_name = 'task'
    success_url = reverse('tasks')
    extra_context = {
        'title': translate('Remove task'),
        'submit': translate('Delete'),
        'message': translate('Are you sure delete task '),
    }
    permission_denied_message = translate('Please login')
    success_message = translate('Task was successfully deleted')


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    extra_context = {
        'title': translate('Task view'),
        'author': translate('Author'),
        'executor': translate('Executor'),
        'status': translate('Status'),
        'created': translate('Created'),
    }
    permission_denied_message = translate('Please login')
