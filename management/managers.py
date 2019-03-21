"""
Manages all queries related to database model
"""
from management.models import Student, CollegeClass
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


class StudentManager(models.Manager):
    """
    This class manages all the custom queries for Student model
    """

    @classmethod
    def get_all_students(cls):
        """
        fetch all students
        :return:
        """
        try:
            return list(Student.objects.all())
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_student_by_usn(cls, usn):
        """
        get student record by usn
        :param usn:
        :return:
        """
        try:
            return Student.objects.get(usn=usn)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def add_student(cls, name, usn, email, college_class):
        """
        add a new student record
        :return:
        """
        try:
            student = Student.objects.create(name=name, usn=usn, email=email,
                                             college_class=CollegeClass(name=college_class))
            student.save()
            return student
        except IntegrityError:
            return None
