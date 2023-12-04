'''
    imageFont
'''

from PIL import Image,ImageDraw

img = Image.open('blend1.jpg')
draw = ImageDraw.Draw(img)
w,h = img.size
draw.line((0,0,w,h),fill=128,width=5)
draw.line((0,h,w,0),fill=128,width=5)

img.show()