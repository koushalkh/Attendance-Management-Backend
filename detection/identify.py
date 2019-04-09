import cognitive_face as CF
from .global_variables import personGroupId, Key
import os, urllib
import sqlite3
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.utils import get_column_letter, column_index_from_string
import time
from management.models import Attendance, Period, Student, Subject, TimeSlot, Teacher
from django.utils import timezone

def atte():
    att = Attendance.objects.all()
    print("Attendance object is ", att)
    sub = Subject.objects.get(name="Database")
    print(sub)
    print(Period.objects.get(subject=sub))
    print(Period.objects.all()[0])
    p = Period.objects.all()[0]
    print(p.subject.name)
    # aaa = timezone.now().time()
    # print(aaa, "NOW TIME")
    # print(datetime.datetime.today().weekday())

    # --------------------------------
    # |GET TEACHER FROM THE FRONT END|
    # --------------------------------
    teacher_name = "arnold"


    current_time = timezone.now()
    slot_obj = TimeSlot()
    for slot in TimeSlot.objects.all():
        if current_time >= slot.start_time and current_time <= slot.end_time:
            slot_obj = slot

    teacher_obj = Teacher.objects.get(name=teacher_name)

    #current_period = Period.objects.get(time_slot=slot_obj, teacher=teacher_obj)
    #print(current_period.college_class)

    CF.Key.set(Key)

    connect = connect = sqlite3.connect("Face-DataBase")
    c = connect.cursor()

    attend = [0 for i in range(60)]

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
            print(filename)
            print(res)
            for face in res:
                if not face['candidates']:
                    print("Unknown")
                else:
                    print("heheheh")
            time.sleep(6)
'''
print
"this is the length ", sheet.max_column
for row in range(2, sheet.max_column + 1):
    # rn = sheet.cell('A%s'% row).value
    rn = sheet['A%s' % row].value
    print
    rn
    if rn is not None:
        rn = rn[-2:]
        if attend[int(rn)] != 0:
            col = getDateColumn()
            sheet['%s%s' % (col, str(row))] = 1

wb.save(filename="reports.xlsx")
# currentDir = os.path.dirname(os.path.abspath(__file__))
# imgurl = urllib.pathname2url(os.path.join(currentDir, "1.jpg"))
# res = CF.face.detect(imgurl)
# faceIds = []
# for face in res:
#   faceIds.append(face['faceId'])

# res = CF.face.identify(faceIds,personGroupId)
# for face in res:
#     personName = CF.person.get(personGroupId, face['candidates']['personId'])
#     print personName
# print res
'''
