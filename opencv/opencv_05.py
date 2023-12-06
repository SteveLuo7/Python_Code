import cv2 as cv

def face_detect_demo():
    #   pic to GREY
    grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #   load stat
    face_detector = cv.CascadeClassifier('D:\OpenCV\sources\data\haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(grey)
    for x,y,w,h in faces:
        cv.rectangle(grey,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
    cv.imshow('grey',grey)

#   load pic
img = cv.imread('lena.jpg')
face_detect_demo()
# cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows( )