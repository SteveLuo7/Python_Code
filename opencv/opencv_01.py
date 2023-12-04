'''
    openCV
'''
import cv2 as cv

#   read file

img = cv.imread('lena.jpg')
#   display pic
cv.imshow('read_img',img)
#   wait until keyboard
cv.waitKey(3000)
#   release the ram
cv.destroyAllWindows()