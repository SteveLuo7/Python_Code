import cv2 as cv

img = cv.imread('lena.jpg')

#   draw
x,y,w,h = 50,50,80,80
cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=2)     #   color=BGR

x,y,r = 200,200,100
cv.circle(img,center=(x,y),radius=r,color=(0,0,255),thickness=2)


cv.imshow('rectangle',img)
cv.waitKey(0)
cv.destroyAllWindows()


