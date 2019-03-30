from django.db import models

# Create your models here.
class Person(models.Model):
    """
    Model representing person entity
    """
    usn = models.CharField(max_length=240, primary_key=True)
    person_id = models.CharField(max_length=240)

    def __str__(self):
        return self.usn
