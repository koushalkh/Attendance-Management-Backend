"""
This module maps API urls with API views
"""
from django.urls import path
from .views import login, subjects, student, attendance

urlpatterns = [
    path('login/', login),
    path('subjects/', subjects),
    path('student/', student),
    path('attendance/', attendance)
]
