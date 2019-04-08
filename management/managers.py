"""
Manages all queries related to database model
"""
from management.models import Student, CollegeClass, StudentSubject, Attendance, \
    Teacher, Period, PeriodTracker
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import datetime

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


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

    @classmethod
    def get_student_by_name(cls, name):
        """
        fetch student details by name
        :param name:
        :return:
        """
        try:
            student = Student.objects.get(name=name)
            return student
        except ObjectDoesNotExist:
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
    This manager class handles all queries for Attendance model
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


class TeacherManager(models.Manager):
    """
    This manager class handles all queries for Teacher model
    """

    @classmethod
    def get_teacher_by_name(cls, name):
        """
        get teacher object by name
        :param name:
        :return:
        """
        try:
            teacher = Teacher.objects.get(name=name)
            return teacher
        except ObjectDoesNotExist:
            return None

    @classmethod
    def fetch_daily_periods(cls, name):
        """
        fetch periods taken by a teacher on a given day
        :param name:
        :return:
        """
        current_date = datetime.date.today().weekday()
        current_day = week_days[4]
        try:
            requested_teacher = Teacher.objects.get(name=name)
        except ObjectDoesNotExist:
            return None
        try:
            periods = Period.objects.filter(teacher=requested_teacher)
        except ObjectDoesNotExist:
            return None
        # filter for periods on the current day
        daily_periods = []
        for period in periods:
            if period.time_slot.day == current_day:
                daily_periods.append(period)
        return daily_periods


class PeriodTrackerManager(models.Manager):
    """
    This manager class handles all the queries for PeriodTracker
    """

    @classmethod
    def past(cls, name):
        """
        fetch past classes taken by teacher
        :param name:
        :return:
        """
        daily_periods = TeacherManager.fetch_daily_periods(name)
        if daily_periods is None:
            return None
        past_periods = []
        for period in daily_periods:
            try:
                period_tracker = PeriodTracker.objects.get(period=period)
                if period_tracker is not None and period_tracker.taken is True:
                    past_periods.append(period)
            except ObjectDoesNotExist:
                continue
        return past_periods

    @classmethod
    def upcoming(cls, name):
        """
        fetch upcoming classes for a teacher
        :param name:
        :return:
        """
        daily_periods = TeacherManager.fetch_daily_periods(name)
        print(daily_periods)
        if daily_periods is None:
            return None
        upcoming_periods = []
        for period in daily_periods:
            try:
                period_tracker = PeriodTracker.objects.get(period=period)
                print("hello")
                print(period_tracker.taken)
                if period_tracker.taken is False:
                    upcoming_periods.append(period)
            except ObjectDoesNotExist:
                continue
        return upcoming_periods
