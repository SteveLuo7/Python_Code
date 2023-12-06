import cv2
import numpy as np
import os

#   load the trained file
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/train.yml')
#   ready to recognizer pic
img = cv2.imread('12.pgm')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier('D:/OpenCV/sources/data/haarcascades/haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(grey)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    #   recognize human face
    id,confidence = recognizer.predict(grey[y:y+h,x:x+2])
    print('LabelID: ',id,'Confidence: ',confidence)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()