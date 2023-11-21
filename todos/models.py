{
  "codeChangeList": [
    {
      "filePath": "todos/models.py",
      "code": """
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)  # New TextField to store the body of the note
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
"""
    }
  ]
}
