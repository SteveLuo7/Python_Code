from PIL import Image,ImageDraw,ImageFont

img = Image.open('lena.jpg')
draw = ImageDraw.Draw(img)

w,h = img.size

draw.arc((0,0,w-1,h-1),0,360,fill='blue')
img.save('circle.jpg')