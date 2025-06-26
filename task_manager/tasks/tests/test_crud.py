from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.tasks.models import Task
from task_manager.test_db import TestDB


class TestTask(TestDB, TestCase):
    def test_task_page_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)

    def test_task_page_logout(self):
        response = self.client.get(reverse("tasks"))
        self.assertRedirects(response, "/login/?next=/tasks/")

    def test_create_task(self):
        new_task_data = {
            "name": "test2",
            "author": self.user.id,
            "status": self.status.id,
        }
        tasks_count = Task.objects.all().count()
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("task_create"), new_task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("tasks"))
        new_task = Task.objects.last()
        self.assertEqual(new_task.name, new_task_data.get("name"))
        self.assertEqual(Task.objects.all().count(), tasks_count + 1)

    def test_read_task(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        update_task = {
            "name": "bla",
            "author": self.user.id,
            "status": self.status.id,
        }
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("task_update", kwargs={"pk": self.task.id}),
            update_task,
        )
        self.assertRedirects(response, reverse("tasks"))
        task = Task.objects.get(pk=self.task.id)
        self.assertEqual(task.name, update_task.get("name"))

    def test_delete_task(self):
        tasks_count = Task.objects.all().count()

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("task_delete", kwargs={"pk": self.task.id})
        )
        self.assertRedirects(response, reverse("tasks"))
        self.assertEqual(Task.objects.all().count(), tasks_count - 1)
