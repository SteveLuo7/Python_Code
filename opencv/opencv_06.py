import cv2 as cv

def face_detect_demo():
    grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('D:/OpenCV/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(grey,scaleFactor=1.01,minNeighbors=3)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+h,y+h),color=(0,0,255),thickness=2)
        cv.circle(img,center=(x+w//2,y+w//2),radius=w//2,color=(0,255,0),thickness=2)

    cv.imshow('result',img)



img = cv.imread('face.jpg')
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
