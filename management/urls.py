"""
This module maps API urls with API views
"""
from django.urls import path
from .views import login, subjects, student, attendance, teacher, \
    daily_periods, upcoming_periods, past_periods

urlpatterns = [
    path('login/', login),
    path('subjects/', subjects),
    path('student/', student),
    path('attendance/', attendance),
    path('teacher/', teacher),
    path('periods/', daily_periods),
    path('periods/upcoming/', upcoming_periods),
    path('periods/past/', past_periods),
]
