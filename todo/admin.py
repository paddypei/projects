from __future__ import unicode_literals
from django.contrib import admin
from todo.models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
     list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
     list_filter = ('pubtime',)
     ordering = ('-pubtime',)


admin.site.register(Todo, TodoAdmin)