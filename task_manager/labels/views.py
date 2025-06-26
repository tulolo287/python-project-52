from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.labels.forms import LabelForm
from task_manager.labels.mixins import CheckTaskMixin
from task_manager.labels.models import Label


class IndexLabelView(LoginRequiredMixin, ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = "labels"
    extra_context = {
        "title": translate("Labels"),
        "ID": translate("ID"),
        "name": translate("Name"),
        "edit": translate("Edit"),
        "delete": translate("Delete"),
        "created_at": translate("Created at"),
        "submit": translate("Create label"),
    }
    permission_denied_message = translate("Please login")


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = "form.html"
    success_url = reverse("labels")
    extra_context = {
        "title": translate("Create label"),
        "submit": translate("Create"),
    }
    success_message = translate("Label has been created successfully")


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "form.html"
    success_url = reverse("labels")
    extra_context = {
        "title": translate("Update label"),
        "submit": translate("Update"),
    }
    success_message = translate("Label has been edited successfully")


class DeleteLabelView(
    LoginRequiredMixin, SuccessMessageMixin, CheckTaskMixin, DeleteView
):
    model = Label
    context_object_name = "label"
    template_name = "labels/delete.html"
    success_url = reverse("labels")
    extra_context = {
        "title": translate("Delete label"),
        "submit": translate("Yes, delete"),
        "confirm": translate("Are you sure delete"),
    }
    success_message = translate("Label was successfully deleted")
    protected_error_message = translate(
        "You cannot delete a label which is currently being used"
    )
