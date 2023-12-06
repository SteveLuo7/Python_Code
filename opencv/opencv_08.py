import cv2
import cv2 as cv
import os
import sys
from PIL import Image
import numpy as np
def getImageAndLabels(path):
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)
    #   travel all the pic in the list
    for imagePath in imagePaths:
        #   open the pic
        PIL_img = Image.open(imagePath).convert('L')
    #   transfer pic to tuple
    img_numpy = np.array(PIL_img,'uint8')
    face_detector = cv.CascadeClassifier('D:/OpenCV/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(img_numpy)
    id = int(os.path.split(imagePath)[1].split('.')[0])
    for x,y,w,h in faces:
        facesSamples.append(img_numpy[y:y+h,x:x+w])
        ids.append(id)

    return facesSamples,ids


if __name__ == '__main__':
    path = './data/jm'
    #   get img and id
    faces,ids = getImageAndLabels(path)
    #   get loop element
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces,np.array(ids))
    #   save files
    recognizer.write('trainer/train.yml')
