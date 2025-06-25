from django import forms
from django.utils.translation import gettext_lazy as translate
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        label=translate("Status"), queryset=Status.objects.all()
    )
    executor = ModelChoiceFilter(
        label=translate("Executor"), queryset=User.objects.all()
    )
    labels = ModelChoiceFilter(
        label=translate("Label"), queryset=Label.objects.all()
    )
    my_tasks_only = BooleanFilter(
        label=translate("My tasks"),
        widget=forms.CheckboxInput,
        method="get_my_tasks",
    )

    def get_my_tasks(self, queryset, _, value):
        tasks = queryset.filter(author_id=self.request.user.id)
        return tasks if value else queryset

    class Meta:
        model = Task
        fields = ("status", "executor", "labels")
