import json
import os

from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.statuses.models import Status
from task_manager.users.models import User

FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "fixtures",
)


class TestStatus(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixture_file = os.path.join(FIXTURES_DIR, "status.json")
        with open(fixture_file, "r") as fixtures:
            cls.status_data = json.load(fixtures)
        cls.test_status = Status.objects.create(**cls.status_data)
        user_data = {
            "first_name": "user2",
            "last_name": "user2",
            "username": "test2@test.com",
            "password": "user2"
        }
        cls.user = User.objects.create_user(**user_data)

    def test_status_page_status_200(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)

    def test_create_status(self):
        new_status_data = {
            "name": "test2",
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("status_create"), new_status_data)

        self.assertRedirects(response, reverse("statuses"))
        status2 = Status.objects.get(pk=2)
        self.assertEqual(status2.name, new_status_data.get("name"))
        self.assertEqual(Status.objects.all().count(), 2)

    def test_read_status(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")

    def test_update_status(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("status_update", kwargs={"pk": self.test_status.id}),
            self.status_data,
        )
        self.assertRedirects(response, reverse("statuses"))
        status = Status.objects.get(pk=self.test_status.id)
        self.assertEqual(status.name, self.status_data.get("name"))

    def test_delete_status(self):
        self.assertEqual(Status.objects.all().count(), 1)

        self.client.force_login(user=self.user)
        response = self.client.post(reverse("status_delete", kwargs={"pk": self.test_status.id}))
        self.assertRedirects(response, reverse("statuses"))
        self.assertEqual(Status.objects.all().count(), 0)
