from django.test import TestCase
from .models import Student


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
        Student.objects.create(name="john", usn="1RN15CS098", email="john@gmail.com", class_name="8A")
        Student.objects.create(name="sam", usn="1RN15CS075", email="sam@gmail.com", class_name="8B")

    def test_get_all_students(self):
        num_of_students = len(Student.objects.all())
        self.assertsEqual(num_of_students,2)
