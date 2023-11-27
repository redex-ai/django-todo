from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title
