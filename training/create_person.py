import sys
import cognitive_face as CF
from global_variables import personGroupId, Key
import sqlite3
from .models import Person

def create_person(usn):
    CF.Key.set(Key)
    res = CF.person.create(personGroupId, usn)
    print(res)
    Person.objects.filter(usn=usn).update(person_id=res['personId'])
    print("Person ID successfully added to the database")
    