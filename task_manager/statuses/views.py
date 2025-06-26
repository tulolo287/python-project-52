from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.labels.mixins import CheckTaskMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/index.html"
    extra_context = {
        "title": translate("Statuses"),
        "ID": translate("ID"),
        "name": translate("Name"),
        "edit": translate("Edit"),
        "delete": translate("Delete"),
        "created_at": translate("Created at"),
        "create_status": translate("Create status"),
    }
    permission_denied_message = translate("Please login")


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "form.html"
    success_url = reverse("statuses")
    extra_context = {
        "title": translate("Create status"),
        "submit": translate("Create"),
    }
    success_message = translate("Status created successfully")
    permission_denied_message = translate("Please login")


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "form.html"
    success_url = reverse("statuses")
    extra_context = {
        "title": translate("Update status"),
        "submit": translate("Update"),
    }
    success_message = translate("Status successfully changed")
    permission_denied_message = translate("Please login")


class StatusDeleteView(
    CheckTaskMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView
):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/delete.html"
    success_url = reverse("statuses")
    extra_context = {
        "title": translate("Remove status"),
        "confirm": translate("Are you sure delete"),
        "submit": translate("Yes, delete"),
    }
    success_message = translate("Status was deleted successfully")
    permission_denied_message = translate("Please login")
    protected_error_message = translate("Cannot delete busy status")
