```
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from .forms import TodoForm

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
```
