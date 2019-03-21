from django.test import TestCase
from .models import Student, CollegeClass
from .managers import StudentManager


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


