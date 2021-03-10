from django.contrib import admin
from TodoApp.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['header', 'content','isCompleted', 'timestamp']

admin.site.register(Todo, TodoAdmin)