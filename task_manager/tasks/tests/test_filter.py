from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.test_db import TestDB


class TestFiler(TestDB, TestCase):
    def setUp(self):
        self.client.force_login(user=self.user)
        self.response = self.client.get(reverse_lazy("tasks"))

    def test_filter_exist(self):
        self.assertContains(self.response, "Show")

    def test_filter_not_filtered(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, self.task_data.get("name"))
        self.assertContains(self.response, self.task2_data.get("name"))

    def test_filter_by_status(self):
        query = {"status": self.status.id}
        response = self.client.get(reverse_lazy("tasks"), data=query)
        self.assertContains(response, self.task_data.get("name"))
        self.assertNotContains(response, self.task2_data.get("name"))

    def test_filter_by_executor(self):
        query = {"executor": self.user2.id}
        response = self.client.get(reverse_lazy("tasks"), data=query)
        self.assertContains(response, self.task_data.get("name"))
        self.assertNotContains(response, self.task2_data.get("name"))

    def test_filter_by_label(self):
        query = {"labels": self.label.id}
        response = self.client.get(reverse_lazy("tasks"), data=query)
        self.assertContains(response, self.task_data.get("name"))
        self.assertNotContains(response, self.task2_data.get("name"))
