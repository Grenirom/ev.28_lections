from django.contrib import admin

from study.models import Student, Course

admin.site.register(Course)
admin.site.register(Student)