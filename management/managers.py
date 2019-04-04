"""
Manages all queries related to database model
"""
from management.models import Student, CollegeClass, StudentSubject, Attendance
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


class StudentSubjectManager(models.Manager):
    """
    This manager class handles all queries for Subject models
    """

    @classmethod
    def get_all_subjects_by_student(cls, usn):
        """
        fetch all subjects selected by student
        :return:
        """
        try:
            # Get the student details using USN
            student = Student.objects.get(usn=usn)
            subjects = StudentSubject.objects.filter(student=student)
            return subjects
        except ObjectDoesNotExist:
            return None


class AttendanceManager(models.Manager):
    """
    This model handles all queries for Attendance model
    """

    @classmethod
    def get_attendance_of_student(cls, student):
        """
        fetch attendance of a student by student object
        :param student:
        :return:
        """
        try:
            attendance = list(Attendance.objects.filter(student=student))
            return attendance
        except ObjectDoesNotExist:
            return None
