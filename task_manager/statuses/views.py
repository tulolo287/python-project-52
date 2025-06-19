from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/index.html"
    extra_context = {
        'title': translate('Statuses'),
        'ID': translate('ID'),
        'name': translate('Name'),
        'edit': translate('Edit'),
        'delete': translate('Delete'),
        'created_at': translate('Created at'),
        'create_status': translate('Create status'),
    }
    permission_denied_message = translate('Please login')


class StatusCreateView(LoginRequiredMixin, CreateView):
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "statuses/create.html"
    success_url = reverse('statuses')
    extra_context = {
        'title': translate('Create status'),
        'submit': translate('Create'),
    }
    success_message = translate('Status created successfully')
    permission_denied_message = translate('Please login')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "statuses/update.html"
    success_url = reverse('statuses')
    extra_context = {
        'title': translate('Update status'),
        'submit': translate('Update'),
    }
    success_message = translate('Status updated successfully')
    permission_denied_message = translate('Please login')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/delete.html"
    success_url = reverse('statuses')
    extra_context = {
        'title': translate('Remove status'),
        'confirm': translate('Are you sure delete'),
        'submit': translate('Yes, remove'),
    }
    permission_denied_message = translate('Please login')
    protected_error_message = translate('Status can\'t be deleted - on use now')
    success_message = translate('Status was deleted successfully')
