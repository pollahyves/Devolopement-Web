from django.contrib import admin
from .models import Task

# Register your models here.

class AdminTask(admin.ModelAdmin):
    list_display = ['amount','bank','date']


admin.site.register(Task,AdminTask)
