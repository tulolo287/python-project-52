from django import forms
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as translate


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": translate("name"),
                }
            ),
        }
        labels = {"name": translate("Name")}
