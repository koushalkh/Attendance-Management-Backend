"""
This module defines all the serializers used in management app
"""
from .models import Subject
from rest_framework import serializers


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Subject data
    """
    class Meta:
        model = Subject
