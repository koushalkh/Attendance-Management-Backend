import cognitive_face as CF
from .global_variables import personGroupId, Key
import os, urllib
import sqlite3
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.utils import get_column_letter, column_index_from_string
import time
from datetime import datetime
from management.models import Attendance, Period, Student, Subject, TimeSlot, Teacher
from training.models import Person

def attendance():
    # --------------------------------
    # |GET TEACHER FROM THE FRONT END|
    # --------------------------------
    teacher_name = "arnold"

    current_time = datetime.now().strftime("%H:%M:%S")
    current_time = datetime.strptime(current_time, "%H:%M:%S").time()
    print("Current time is ", current_time)

    time_slot_obj = TimeSlot()
    for slot in TimeSlot.objects.all():
        if current_time >= slot.start_time and current_time <= slot.end_time:
            time_slot_obj = slot

    teacher_obj = Teacher.objects.get(name=teacher_name)

    current_period = Period.objects.get(time_slot=time_slot_obj, teacher=teacher_obj)
    print(current_period.college_class)

    CF.Key.set(Key)

    connect = connect = sqlite3.connect("Face-DataBase")
    c = connect.cursor()

    currentDir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(currentDir, 'Cropped_faces')
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            imgurl = urllib.request.pathname2url(os.path.join(directory, filename))
            res = CF.face.detect(imgurl)
            if len(res) != 1:
                print("No face detected.")
                continue

            faceIds = []
            for face in res:
                faceIds.append(face['faceId'])
            res = CF.face.identify(faceIds, personGroupId)
            # print(filename)
            # print(res)
            for face in res:
                if not face['candidates']:
                    print("Unknown")
                else:
                    personId = face['candidates'][0]['personId']
                    print(personId)
                    usn = Person.objects.get(person_id = personId).usn
                    print(usn)
                    student = Student.objects.get(usn = usn)
                    current_date = datetime.today().date()
                    attendance = Attendance(period=current_period,
                                            student = student,
                                            present_date = current_date)
                    attendance.save()
                    print("Attendance marked successfully for ", student.name)
            time.sleep(6)
