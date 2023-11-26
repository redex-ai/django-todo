from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_at', 'update_at', 'isCompleted')

admin.site.register(Todo, TodoAdmin)
