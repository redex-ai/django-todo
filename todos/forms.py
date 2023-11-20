{
  "codeChangeList": [
    {
      "filePath": "todos/models.py",
      "code": """
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)  # New field for storing longer text content
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
"""
    },
    {
      "filePath": "todos/forms.py",
      "code": """
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body', 'isCompleted']  # Include the body field

    def save(self, commit=True):
        todo = super(TodoForm, self).save(commit=False)
        if commit:
            todo.save()
        return todo
"""
    }
  ]
}
