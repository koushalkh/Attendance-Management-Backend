import cognitive_face as CF
from .global_variables import personGroupId, Key
import sys

def create_group():
	CF.Key.set(Key)

	personGroups = CF.person_group.lists()
	for personGroup in personGroups:
		if personGroupId == personGroup['personGroupId']:
			return

	res = CF.person_group.create(personGroupId)

