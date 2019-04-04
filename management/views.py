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
    HTTP_200_OK
)
from rest_framework.response import Response
# from .managers import

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


# @api_view(["GET"])
# def getSubjects(request):
#     try:

