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
from .managers import StudentSubjectManager, StudentManager, AttendanceManager, \
    TeacherManager, PeriodTrackerManager
from .serializers import StudentSubjectSerializer, SubjectSerializer, StudentSerializer, \
    AttendanceSerializer, TeacherSerializer, PeriodSerializer


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
    # Send the type of person
    person_type = "management"
    # Check if the person belongs to student group
    check_for_student = StudentManager.get_student_by_name(username)
    if check_for_student is not None:
        person_type = "student"
    check_for_teacher = TeacherManager.get_teacher_by_name(username)
    if check_for_teacher is not None:
        person_type = "teacher"
    # send token credentials if the user is logged in
    print({'token': token.key, 'type': person_type})
    return Response({'token': token.key, 'type': person_type}, status=HTTP_200_OK)


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
    """
    API endpoint to fetch student details by USN
    :param request:
    :return:
    """
    usn = request.data['usn']
    requested_student = StudentManager.get_student_by_usn(usn)
    if requested_student is None:
        return Response("USN not found", status=HTTP_400_BAD_REQUEST)
    serializer = StudentSerializer(requested_student)
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def attendance(request):
    """
    API endpoint to fetch attendance of given student
    :param request:
    :return:
    """
    usn = request.data['usn']
    requested_student = StudentManager.get_student_by_usn(usn)
    requested_attendance = AttendanceManager.get_attendance_of_student(requested_student)
    print(requested_attendance)
    serializer = AttendanceSerializer(requested_attendance, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def teacher(request):
    """
    API endpoint to fetch teacher details
    :param request:
    :return:
    """
    name = request.data['name']
    requested_teacher = TeacherManager.get_teacher_by_name(name)
    if requested_teacher is None:
        return Response("Teacher not found", status=HTTP_400_BAD_REQUEST)
    serializer = TeacherSerializer(requested_teacher)
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def daily_periods(request):
    """
    API endpoint to fetch daily class periods of a requested teacher
    :param request:
    :return:
    """
    name = request.data['name']
    periods = TeacherManager.fetch_daily_periods(name)
    if periods is None:
        return Response("Invalid details", status=HTTP_400_BAD_REQUEST)
    serializer = PeriodSerializer(periods, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def upcoming_periods(request):
    """
    API end point to fetch upcoming periods on current day
    :param request:
    :return:
    """
    name = request.data['name']
    requested_teacher = TeacherManager.get_teacher_by_name(name)
    if requested_teacher is None:
        return Response("Invalid name", status=HTTP_400_BAD_REQUEST)
    upcoming = PeriodTrackerManager.upcoming(name)
    if upcoming is None:
        return Response("No upcoming periods", status=HTTP_400_BAD_REQUEST)
    serializer = PeriodSerializer(upcoming, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def past_periods(request):
    """
    API end point to fetch past period taken by teacher on the current day
    :param request:
    :return:
    """
    name = request.data['name']
    requested_teacher = TeacherManager.get_teacher_by_name(name)
    if requested_teacher is None:
        return Response("Invalid name", status=HTTP_400_BAD_REQUEST)
    past = PeriodTrackerManager.past(name)
    if past is None:
        return Response("No periods taken", status=HTTP_400_BAD_REQUEST)
    serializer = PeriodSerializer(past, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
