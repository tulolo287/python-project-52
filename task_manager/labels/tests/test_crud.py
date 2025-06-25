from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.test_db import TestDB


class TestLabels(TestDB, TestCase):

    def test_labels_index_page_not_loggedIn(self):
        response = self.client.get(reverse_lazy('labels'))
        self.assertRedirects(response, expected_url='/login/?next=/labels/')

    def test_labels_index_page_loggedIn(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 200)

    def test_create_label(self):
        new_label_data = {'name': 'new-label'}
        total_labels = Label.objects.all().count()
        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy('label_create'), new_label_data)

        self.assertRedirects(response, expected_url=(reverse_lazy('labels')))
        new_label = Label.objects.last()
        self.assertEqual(new_label.name, new_label_data.get('name'))
        self.assertEqual(Label.objects.all().count(), total_labels + 1)

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
        response = self.client.post(
            reverse_lazy('label_delete', kwargs={'pk': self.label.id})
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'User was successfully deleted')

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

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You cannot delete a label which is currently being used.'
        )

        self.assertRedirects(response, expected_url=reverse_lazy('labels'))
        self.assertEqual(Label.objects.all().count(), total_labels)
