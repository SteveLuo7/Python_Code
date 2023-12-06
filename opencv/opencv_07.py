import cv2 as cv
import numpy as np

def face_detect_demo(img):
    grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('D:/OpenCV/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(grey)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

#   read the video
cap = cv.VideoCapture('video.mp4')
while True:
    flag,frame = cap.read()
    print('flag: ',flag,'frame_shape: ',frame.shape)
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(10):
        break


cv.destroyAllWindows()
cap.release()

