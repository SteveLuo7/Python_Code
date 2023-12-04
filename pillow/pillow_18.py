from PIL import Image,ImageDraw
w,h = 300,300
img = Image.new('RGB',(w,h),'white')

draw = ImageDraw.Draw(img)

def get_color(x,y):
    a = x//100 + y//100
    if a == 0:
        return (255,0,0)
    elif a == 1:
        return (255,255,0)
    elif a == 2:
        return (255,255,255)
    elif a == 3:
        return (0,0,255)
    elif a == 4:
        return (0,255,255)
    else:
        return (0,0,0)

for x in range(w):
    for y in range(h):
        draw.point((x,y),fill=get_color(x,y))



img.show()



