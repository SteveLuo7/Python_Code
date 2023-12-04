from PIL import Image,ImageDraw,ImageFont

img = Image.open('bjsxt.png')
w,h = img.size

draw = ImageDraw.Draw(img)

def get_color(oldColor):
    # print(oldColor)
    #   get all yellow elements
    if oldColor[0]>60 and oldColor[1]>60:
        return (oldColor[0],0,oldColor[2])  #   return red
    else:
        return oldColor
for x in range(w):
    for y in range(h):
        oldColor = img.getpixel((x,y))
        draw.point((x,y),fill=get_color(oldColor))

img.show()