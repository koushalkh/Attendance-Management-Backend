"""
Register models in management app
"""
from django.contrib import admin
from .models import Teacher, Period, TimeSlot, \
    Subject, StudentSubject, Student, CollegeClass, Attendance

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Period)
admin.site.register(TimeSlot)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(Student)
admin.site.register(CollegeClass)
admin.site.register(Attendance)
