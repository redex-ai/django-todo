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
    },
    {
      "filePath": "todos/admin.py",
      "code": """
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_at', 'update_at', 'isCompleted')  # Register the new body field

admin.site.register(Todo, TodoAdmin)
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
        fields = ['title', 'body', 'isCompleted']  # Add the body field to the TodoForm
"""
    },
    {
      "filePath": "todos/views.py",
      "code": """
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from .forms import TodoForm  # Import TodoForm
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    return render(request, 'todos/add.html', {'form': form})

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/update.html', {'form': form})
"""
    }
  ]
}
