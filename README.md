### Hexlet tests and linter status:
[![Actions Status](https://github.com/tulolo287/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tulolo287/python-project-52/actions)


import json
import os

from django.test import TestCase
from django.urls import reverse_lazy as reverse

from task_manager.users.models import User

FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixture_file = os.path.join(FIXTURES_DIR, "user.json")
        with open(fixture_file, "r") as fixtures:
            cls.user_data = json.load(fixtures)
        cls.user_create_data = dict(list(cls.user_data.items())[:-2])
        cls.mock_user = User.objects.create_user(**cls.user_data)
        cls.mock_user_create = User.objects.create_user(**cls.user_create_data)


    def test_users_page_status_200(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(reverse("user_create"), self.user_data)

        self.assertRedirects(response, reverse("login"))
        user = User.objects.get(pk=1)
        print("KJKJKJKJKK", self.user_data)
        self.assertEqual(user.username, self.user_data.get("username"))

    def test_read_user(self):
        #User.objects.create_user(**self.mock_create_user)
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_create_data.get('username'))
        self.assertContains(response, self.user_create_data.get('first_name'))
        self.assertContains(response, self.user_create_data.get('last_name'))

    def test_update_user(self):
        pass
        #response = self.client.post(reverse("user_update"), self.mock_user)
