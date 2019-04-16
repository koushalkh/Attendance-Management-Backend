"""
Register models in management app
"""
from django.contrib import admin
from .models import Student, CollegeClass, Teacher, TimeSlot \
    , Subject, StudentSubject, Period, Attendance, PeriodTracker

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Period)
admin.site.register(TimeSlot)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(Student)
admin.site.register(CollegeClass)
admin.site.register(Attendance)
admin.site.register(PeriodTracker)

# Custom header for management
admin.site.site_header = "RNSIT Management"
admin.site.site_title = "RNSIT"
admin.site.index_title = "Welcome to attendance management portal"

# Add functionalty for button on Admin home page
