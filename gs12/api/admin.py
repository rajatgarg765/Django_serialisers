from atexit import register
from django.contrib import admin

# Register your models here.
from api.models import Student

@admin.register(Student)
class StudAdmin(admin.ModelAdmin):
    list_display=['name']