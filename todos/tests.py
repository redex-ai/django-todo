from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoTests(TestCase):
    def test_add_todo_with_body(self):
        response = self.client.post(reverse('todos:add'), {'title': 'Test Todo', 'body': 'Test Body'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.first()
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.body, 'Test Body')

    def test_add_todo_without_body(self):
        response = self.client.post(reverse('todos:add'), {'title': 'Test Todo'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.first()
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.body, '')

    def test_update_todo_with_body(self):
        todo = Todo.objects.create(title='Test Todo')
        response = self.client.post(reverse('todos:update', args=[todo.id]), {'isCompleted': 'on', 'body': 'Updated Body'})
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.isCompleted, True)
        self.assertEqual(todo.body, 'Updated Body')

    def test_update_todo_without_body(self):
        todo = Todo.objects.create(title='Test Todo')
        response = self.client.post(reverse('todos:update', args=[todo.id]), {'isCompleted': 'on'})
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.isCompleted, True)
        self.assertEqual(todo.body, '')
