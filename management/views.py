"""
This module handles all the APIs for management app
"""
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED

)
from rest_framework.response import Response
from .managers import StudentSubjectManager, StudentManager, AttendanceManager
from .serializers import StudentSubjectSerializer, SubjectSerializer, StudentSerializer, \
    AttendanceSerializer


# Create your views here.

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    View for user authentication
    :param request:
    :return:
    """
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    # send token credentials if the user is logged in
    return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def subjects(request):
    """
    API endpoint to fetch all subjects taken by a student
    :param request:
    :return:
    """
    student_subjects = StudentSubjectManager.get_all_subjects_by_student(request.data['usn'])
    all_subjects = []
    if student_subjects is None:
        return Response("", status=HTTP_400_BAD_REQUEST)
    for subject in student_subjects:
        all_subjects.append(subject.subject)
    serializers = SubjectSerializer(all_subjects, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def student(request):
    usn = request.data['usn']
    requested_student = StudentManager.get_student_by_usn(usn)
    if requested_student is None:
        return Response("USN not found", status=HTTP_400_BAD_REQUEST)
    serializer = StudentSerializer(requested_student)
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def attendance(request):
    usn = request.data['usn']
    requested_student = StudentManager.get_student_by_usn(usn)
    requested_attendance = AttendanceManager.get_attendance_of_student(requested_student)
    print(requested_attendance)
    serializer = AttendanceSerializer(requested_attendance, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
