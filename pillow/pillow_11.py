from PIL import Image
img = Image.open('blend1.jpg')
w,h = img.size

img_output = Image.new('RGB',(3*w,h))
img_output.paste(img,(0,0))

#   use point()

imgb = img.point(lambda i:i*1.5)

imgc = img.point(lambda i:i*0.2)

img_output.paste(imgb,(w,0))
img_output.paste(imgc,(2*w,0))

img_output.show()