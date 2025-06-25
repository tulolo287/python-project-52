from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.test_db import TestDB
from task_manager.users.models import User


class TestUser(TestDB, TestCase):

    def users_page_status_200(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        new_user_data = {
            "first_name": "new_user",
            "last_name": "new_user",
            "username": "new_user",
            "password1": "new_user",
            "password2": "new_user",
        }
        total_users = User.objects.count()

        response = self.client.post(reverse("user_create"), new_user_data)
        self.assertRedirects(response, reverse("login"))

        new_user = User.objects.last()
        self.assertEqual(new_user.username, new_user_data.get("username"))
        self.assertEqual(User.objects.all().count(), total_users + 1)

    def test_read_user(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_data.get("username"))
        self.assertContains(response, self.user_data.get("first_name"))
        self.assertContains(response, self.user_data.get("last_name"))

    def test_update_user(self):
        password = self.user_data.get('password')
        update_user = {
            **self.user_data,
            'username': 'blas',
            'password1': password,
            'password2': password,
        }
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("user_update", kwargs={"pk": self.user.id}),
            update_user,
        )
        self.assertRedirects(response, reverse("users"))
        user = User.objects.get(pk=self.user.id)
        self.assertEqual(user.username, update_user.get("username"))

    def test_delete_user(self):
        user = User.objects.create_user('test')
        total_users = User.objects.count()

        self.client.force_login(user=user)
        response = self.client.post(reverse("user_delete", kwargs={"pk": user.id}))

        self.assertRedirects(response, reverse("users"))
        self.assertEqual(User.objects.count(), total_users - 1)
