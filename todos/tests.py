from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoAddTestCase(TestCase):
    def test_add_with_valid_deadline(self):
        response = self.client.post(reverse('todos:add'), {'title': 'Test Todo', 'deadline': '2022-12-31'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.first()
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.deadline, '2022-12-31')

    def test_add_with_invalid_deadline(self):
        response = self.client.post(reverse('todos:add'), {'title': 'Test Todo', 'deadline': 'invalid-date'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 0)
