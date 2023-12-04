'''
    rotate and covert
'''

from PIL import Image

img = Image.open('bjsxt.png')
#   rotate
img.rotate(180).show()


#   transpose
img.transpose(Image.FLIP_TOP_BOTTOM).show()    #top and bottom
img.transpose(Image.FLIP_LEFT_RIGHT).show()    #top and bottom
img.transpose(Image.ROTATE_90).show()

#   convert
img.convert(mode='RGB').show()