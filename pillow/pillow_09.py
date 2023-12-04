'''
    imagechops
'''

from PIL import Image,ImageChops

img1 = Image.open('blend1.jpg')
img2 = Image.open('blend2.jpg')

#   plus 2 diferent pictures
ImageChops.add(img1,img2).show()

ImageChops.subtract(img1,img2).show()

ImageChops.darker(img1,img2).show()

ImageChops.lighter(img1,img2).show()

ImageChops.multiply(img1,img2).show()

#   screen
ImageChops.screen(img1,img2).show()

ImageChops.invert(img1).show()