import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import dlib
import os
from .create_person_group import create_group
from .create_person import create_person
from .add_person_faces import add_person_faces
from .train import train
from .models import Person                                                                       # for creating folders


def insertOrUpdate(usn) :                                            # this function is for database
    try:
        person = Person.objects.get(usn = usn)
    except:
        person = None
    if person == None:
        Person.objects.create(usn = usn)
    print(person)


def add_student():
    print("Entered the function!")
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    #Chane this such that USN is obtained from front end
    print("before input")
    #usn = input("Enter student's USN :").upper()
    usn = "1RN15CS080"
    insertOrUpdate(usn)


    folderName = usn                                                        # creating the person or user folder
    folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    sampleNum = 0
    while(True):
        ret, img = cap.read()                                                       # reading the camera input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
        dets = detector(img, 1)
        for i, d in enumerate(dets):                                                # loop will run for each face detected
            sampleNum += 1
            cv2.imwrite(folderPath + "/" + usn + "." + str(sampleNum) + ".jpg",
                        img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
            cv2.waitKey(200)                                                        # waiting time of 200 milisecond
        cv2.imshow('frame', img)                                                    # showing the video input from camera on window
        cv2.waitKey(1)
        if(sampleNum >= 20):                                                        # will take 20 faces
            break

    cap.release()                                                                   # turning the webcam off
    cv2.destroyAllWindows()                                                         # Closing all the opened windows

    create_group()
    create_person(usn)
    add_person_faces(usn)
    train()

