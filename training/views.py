from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .add_student import add_student

def training(request):
    add_student()
    return HttpResponse("Successfully added student")