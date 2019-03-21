from django.test import TestCase
from .models import Student, CollegeClass, Subject, StudentSubject
from .managers import StudentManager, StudentSubjectManager


# Create your tests here.


class StudentTestCase(TestCase):
    """
    Test cases for Student model
    """

    def setUp(self):
        """
        Initial project setup
        :return:
        """
        college_class = CollegeClass.objects.create(name="8A")
        Student.objects.create(name="john", usn="1RN15CS098", email="john@gmail.com", class_name=college_class)
        Student.objects.create(name="sam", usn="1RN15CS075", email="sam@gmail.com", class_name=college_class)

    def test_get_all_students(self):
        num_of_students = len(Student.objects.all())
        self.assertEquals(num_of_students, 2)

    def test_get_student_by_usn(self):
        # student = Student.objects.get(usn="1RN15CS098")
        student = StudentManager.get_student_by_usn("1RN15CS098")
        self.assertEquals(student.class_name.name, "8A")


class SubjectTestCase(TestCase):
    """
    Test cases for subject-student model
    """

    def setUp(self):
        class_name = CollegeClass.objects.create(name="8A")
        stud = Student.objects.create(name="john", usn="1rn15cs037", email="abc@gmail.com", class_name=class_name)
        s2 = Subject.objects.create(name="Algorithms", subject_id="15cs083")
        s3 = Subject.objects.create(name="ML", subject_id="15cs084")
        StudentSubject.objects.create(subject=s2, student=stud)
        StudentSubject.objects.create(subject=s3, student=stud)

    def test_get_subjects_by_student(self):
        subjects = StudentSubjectManager.get_all_subjects_by_student("1rn15cs037")
        self.assertEquals(len(subjects), 2)

# class AttendanceTestCase(TestCase):
#