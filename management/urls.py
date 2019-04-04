"""
This module maps API urls with API views
"""
from django.urls import path
from .views import login, subjects

urlpatterns = [
    path('login/', login),
    path('subjects/', subjects)
]
