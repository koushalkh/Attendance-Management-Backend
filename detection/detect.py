import cv2
import dlib
import os
import sys
import sqlite3
from .identify import attendance

def detect_faces():
    #cam = cv2.VideoCapture(1)
    detector = dlib.get_frontal_face_detector()

    #GET THE LINK OF THE ATTENDANCE IMAGE FROM THE FRONT END
    img_link = "./detection/pics/test6.jpg"
    img = cv2.imread(img_link)
    dets = detector(img, 1)
    if not os.path.exists('./detection/Cropped_faces'):
        os.makedirs('./detection/Cropped_faces')
    print("detected = " + str(len(dets)))
    for i, d in enumerate(dets):
        cv2.imwrite('./detection/Cropped_faces/face' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()])
    attendance()
