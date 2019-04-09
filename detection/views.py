from django.shortcuts import render
from .detect import detect_faces
from django.http import HttpResponse

# Create your views here.
def detecting(request):
    detect_faces()
    return HttpResponse("Detection completed")
