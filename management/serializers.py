from rest_framework import serializers
from .models import Subject, StudentSubject, Student, Attendance, Period, \
    TimeSlot, Teacher, CollegeClass


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TimeSLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CollegeClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeClass
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    time_slot = TimeSLotSerializer()
    teacher = TeacherSerializer()
    subject = SubjectSerializer()
    college_class = CollegeClassSerializer()

    class Meta:
        model = Period
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    period = PeriodSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
