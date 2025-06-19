import os

from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "fixtures",
)


class TestTask(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_data = {
            "first_name": "user2",
            "last_name": "user2",
            "username": "test2@test.com",
            "password": "user2",
        }
        status = {"name": "test"}
        cls.user = User.objects.create_user(**user_data)
        cls.status = Status.objects.create(**status)
        task_data = {"name": "test", "author": cls.user, "status": cls.status}
        cls.task = Task.objects.create(**task_data)

    def test_task_page_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)

    def test_task_page_logout(self):
        response = self.client.get(reverse('tasks'))
        self.assertRedirects(response, "/login/?next=/tasks/")

    def test_create_task(self):
        new_task_data = {
            "name": "test2",
            "author": self.user.id,
            "status": self.status.id,
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("task_create"), new_task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("tasks"))
        task2 = Task.objects.get(pk=2)
        self.assertEqual(task2.name, new_task_data.get("name"))
        self.assertEqual(Task.objects.all().count(), 2)

    def test_read_task(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        update_task = {"name": "bla", "author": self.user.id, "status": self.status.id}
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("task_update", kwargs={"pk": self.task.id}),
            update_task,
        )
        self.assertRedirects(response, reverse("tasks"))
        task = Task.objects.get(pk=self.task.id)
        self.assertEqual(task.name, update_task["name"])

    def test_delete_task(self):
        self.assertEqual(Task.objects.all().count(), 1)

        self.client.force_login(user=self.user)
        response = self.client.post(reverse("task_delete", kwargs={"pk": self.task.id}))
        self.assertRedirects(response, reverse("tasks"))
        self.assertEqual(Task.objects.all().count(), 0)
