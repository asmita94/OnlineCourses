from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
     list_display = ['id', 'title', 'description','price', 'cate']
     list_filter=['cate','is_active']

admin.site.register(Course,CourseAdmin)
    