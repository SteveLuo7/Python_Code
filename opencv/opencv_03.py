import cv2 as cv

img = cv.imread('lena.jpg')
print('original',img.shape)
resize_img = cv.resize(img,dsize=(1000,1000))
print('NOW:',resize_img.shape)
cv.imshow('resize_img',resize_img)

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()


