from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):

    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author', blank=False, null=False
    )
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False)
    label = models.ManyToManyField(Label, through='TaskToLabel', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskToLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
