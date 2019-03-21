"""
Manages all queries related to database model
"""
from management.models import Student
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

"""
This class manages all the custom queries for Student model
"""


class StudentManager(models.Manager):

    @classmethod
    def get_all_students(cls):
        try:
            return Student.objects.all()
        except ObjectDoesNotExist:
            return None


