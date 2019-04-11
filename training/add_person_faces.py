import sys
import os, time
import cognitive_face as CF
from .global_variables import personGroupId, Key
import urllib
import sqlite3
from .models import Person

def get_person_id(usn):
	person = Person.objects.get(usn=usn)
	return person.person_id


def add_person_faces(usn):
	CF.Key.set(Key)
	currentDir = os.path.dirname(os.path.abspath(__file__))
	imageFolder = os.path.join(currentDir, "dataset/" + usn)
	person_id = get_person_id(usn)
	for filename in os.listdir(imageFolder):
		if filename.endswith(".jpg"):
			print(filename)
			imgurl = urllib.request.pathname2url(os.path.join(imageFolder, filename))
			res = CF.face.detect(imgurl)
			if len(res) != 1:
				print("No face detected in image")
			else:
				res = CF.person.add_face(imgurl, personGroupId, person_id)
				print(res)
			time.sleep(6)
