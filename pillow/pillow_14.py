'''
    ImageFont
'''

from PIL import Image,ImageDraw,ImageFont

img = Image.open('bjsxt.png')
draw = ImageDraw.Draw(img)
#   setting font type
font = ImageFont.truetype('SIMYOU.TTF',15)
#   use fonts
draw.text((30,10),'克莉丝蒂娅奴派',font=font,fill='white')
img.show()
