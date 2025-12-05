from django.contrib import admin

# Register your models here.
from app.models import student_model

class student_admin(admin.ModelAdmin):
    list_display = ['name','age']

admin.site.register(student_model,student_admin)