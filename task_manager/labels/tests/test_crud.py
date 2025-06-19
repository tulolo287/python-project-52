from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TestLabels(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_data = {
            'name': 'test',
            'username': 'test',
            'email': 'test',
            'password': 'test',
        }
        label_data = {'name': 'label'}
        cls.user = User.objects.create_user(user_data)
        cls.label = Label.objects.create(**label_data)
        status = {"name": "test"}
        cls.status = Status.objects.create(**status)

    def test_labels_index_page_not_loggedIn(self):
        response = self.client.get(reverse_lazy('labels'))
        self.assertRedirects(response, expected_url='/login/?next=/labels/')

    def test_labels_index_page_loggedIn(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 200)

    def test_create_label(self):
        label_data = {'name': 'test'}
        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy('label_create'), label_data)
        self.assertRedirects(response, expected_url=(reverse_lazy('labels')))
        new_label = Label.objects.get(pk=2)
        self.assertEqual(new_label.name, label_data.get('name'))
        self.assertEqual(Label.objects.all().count(), 2)

    def test_update_label(self):
        update_label = {'name': 'blas'}
        label_id = self.label.id
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse_lazy('label_update', kwargs={'pk': label_id}), update_label
        )
        self.assertEqual(response.status_code, 302)
        updated_label = Label.objects.get(id=label_id)
        self.assertEqual(updated_label.name, update_label.get('name'))

    def test_delete_label(self):
        total_labels = Label.objects.all().count()
        self.client.force_login(user=self.user)
        self.client.post(reverse_lazy('label_delete', kwargs={'pk': self.label.id}))
        self.assertEqual(Label.objects.all().count(), total_labels - 1)

    def test_delete_task_label(self):
        total_labels = Label.objects.all().count()
        task_data = {"name": "test", "author": self.user, "status": self.status}
        task = Task.objects.create(**task_data)
        task.label.add(self.label)
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse_lazy('label_delete', kwargs={'pk': self.label.id})
        )
        self.assertRedirects(response, expected_url=reverse_lazy('labels'))
        self.assertEqual(Label.objects.all().count(), total_labels)
