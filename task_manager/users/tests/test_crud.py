import json
import os

from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.users.models import User

FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "fixtures",
)


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixture_file = os.path.join(FIXTURES_DIR, "user.json")
        with open(fixture_file, "r") as fixtures:
            cls.user_data = json.load(fixtures)
        cls.user_create_data = dict(list(cls.user_data.items())[:-1])
        cls.test_user = User.objects.create_user(**cls.user_create_data)

    def test_users_page_status_200(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        new_user_data = {
            "first_name": "user2",
            "last_name": "user2",
            "username": "test2@test.com",
            "password": "user2",
            "password_confirm": "user2",
        }
        response = self.client.post(reverse("user_create"), new_user_data)

        self.assertRedirects(response, reverse("login"))
        user2 = User.objects.get(pk=2)
        self.assertEqual(user2.username, new_user_data.get("username"))
        self.assertEqual(User.objects.all().count(), 2)

    def test_read_user(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_create_data.get("username"))
        self.assertContains(response, self.user_create_data.get("first_name"))
        self.assertContains(response, self.user_create_data.get("last_name"))

    def test_update_user(self):
        self.client.force_login(user=self.test_user)
        response = self.client.post(
            reverse("user_update", kwargs={"pk": self.test_user.id}),
            self.user_data,
        )
        self.assertRedirects(response, reverse("users"))
        user = User.objects.get(pk=self.test_user.id)
        self.assertEqual(user.username, self.user_data.get("username"))

    def test_delete_user(self):
        self.assertEqual(User.objects.all().count(), 1)

        self.client.force_login(user=self.test_user)
        response = self.client.post(reverse("user_delete", kwargs={"pk": self.test_user.id}))
        self.assertRedirects(response, reverse("users"))
        self.assertEqual(User.objects.all().count(), 0)
