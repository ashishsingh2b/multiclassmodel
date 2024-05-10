from django.contrib import admin
from myapp .models import Commoninfo,Student,Teacher
# Register your models here.
@admin.register(Commoninfo)
class Commondetails(admin.ModelAdmin):
    list_display = ['fname','lname','city','schoolname','indexno']

@admin.register(Student)
class StudentsDetails(admin.ModelAdmin):
    list_display = ['parentsname','percentage','presentday']

@admin.register(Teacher)
class TeacherDetails(admin.ModelAdmin):
    list_display = ['salary','subjectname']
