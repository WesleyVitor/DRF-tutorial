from django.contrib import admin
from .models import Course, Avaliation
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created', 'active')

@admin.register(Avaliation)
class AvaliationAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'avaliation', 'active', 'created')