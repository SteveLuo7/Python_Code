import cv2 as cv

img = cv.imread('lena.jpg')
cv.imshow('BGR_img',img)

#   modify image toGREY
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey_img',grey_img)

#   save the grey pic
cv.imwrite('grey_lena.jpg',grey_img)

cv.waitKey(0)
cv.destroyAllWindows()

