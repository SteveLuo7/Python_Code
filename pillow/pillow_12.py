from PIL import Image,ImageDraw,ImageFont

img = Image.new('RGB',(300,300),'white')
drw = ImageDraw.Draw(img)
drw.rectangle((50,50,150,150),outline='red')
font = ImageFont.truetype('SIMLI.TTF',15)
drw.text((60,60),'First Draw',fill='green',font=font)

img.show()

