'''
    capcha picture
'''

from PIL import Image,ImageDraw,ImageFont
import random

w = 100
h = 100

img = Image.new('RGB',(w,h),'white')
draw = ImageDraw.Draw(img)

#   random color
def get_color():
    return (random.randint(200,255),random.randint(200,255),random.randint(200,255))

for x in range(w):
    for y in range(h):
        draw.point((x,y),fill=get_color())

#   random text
def get_char():
    return chr(random.randint(65,97))
font = ImageFont.truetype('simsun.ttc',25)
for i in range(4):
    draw.text((10+i*20,40),get_char(),fill=(255,0,0),font=font)



img.show()