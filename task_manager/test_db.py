from unittest import TestCase

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TestDB(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "user",
            "first_name": "user",
            "last_name": "user",
            "password": "user",
        }
        cls.user2_data = {"username": "user2"}
        cls.status_data = {"name": "status"}
        cls.status2_data = {"name": "status2"}
        cls.label_data = {"name": "label"}
        cls.label2_data = {"name": "label2"}

        cls.user = User.objects.create_user(**cls.user_data)
        cls.user2 = User.objects.create_user(**cls.user2_data)
        cls.status = Status.objects.create(**cls.status_data)
        cls.status2 = Status.objects.create(**cls.status2_data)
        cls.label = Label.objects.create(**cls.label_data)
        cls.label2 = Label.objects.create(**cls.label2_data)

        cls.task_data = {
            "name": "task",
            "status": cls.status,
            "author": cls.user,
            "executor": cls.user2,
        }
        cls.task = Task.objects.create(**cls.task_data)
        cls.task2_data = {
            "name": "task2",
            "status": cls.status2,
            "author": cls.user2,
            "executor": cls.user,
        }
        cls.task2 = Task.objects.create(**cls.task2_data)
