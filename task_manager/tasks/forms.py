from django import forms
from django.utils.translation import gettext_lazy as translate

from task_manager.statuses.models import Status
from task_manager.users.models import User
from .models import Task
from ..labels.models import Label


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["executor"].queryset = User.objects.all()
        self.fields["executor"].label_from_instance = (
            lambda obj: obj.get_full_name()
        )
        self.fields["labels"].queryset = Label.objects.all()

    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": translate("Name"),
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": translate("Description"),
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-control",
                    "choices": Status,
                }
            ),
            "executor": forms.Select(
                attrs={
                    "class": "form-control",
                    "choices": User,
                }
            ),
            "labels": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                    "choices": Label,
                }
            ),
        }
        labels = {
            "name": translate("Name"),
            "description": translate("Description"),
            "status": translate("Status"),
            "executor": translate("Executor"),
            "labels": translate("Labels"),
        }
