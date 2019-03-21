"""
This module contains all the models required for management app
"""
from django.db import models


# Create your models here.


class CollegeClass(models.Model):
    """
    Model representing class entity
    """
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Model representing student entity
    """
    name = models.CharField(max_length=240)
    usn = models.CharField(max_length=240)
    email = models.EmailField()
    class_name = models.ForeignKey(CollegeClass, on_delete=models.CASCADE)

    student = models.Manager

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """
    Model representing Teacher entity
    """
    name = models.CharField(max_length=240)
    email = models.EmailField()

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    """
    Model representing time slot of each period
    """
    day = models.CharField(max_length=240)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.day + ' ' + self.time


class Subject(models.Model):
    """
    Model representing Subject entity
    """

    name = models.CharField(max_length=240)
    subject_id = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Period(models.Model):
    """
    Model representing each instance of a period
    """

    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    college_class = models.OneToOneField(CollegeClass, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.teacher + '' + self.subject


class Attendance(models.Model):
    """
    Model for calculating attendance of each student
    """

    period = models.OneToOneField(Period, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name


class StudentSubject(models.Model):
    """
    Class representing ManyToMany relationship between subject and student
    """

    class Meta:
        """
        subject and student fields must be composite key
        """
        unique_together = ('subject', 'student')

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.name + ' ' + self.student.name
