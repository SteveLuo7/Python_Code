from PIL import Image,ImageEnhance

img1 = Image.open('blend1.jpg')
w,h = img1.size
img_output = Image.new('RGB',(3*w,h))

#   place orignal picture to (0,0)
img_output.paste(img1,(0,0))

#   get ImageEnhance
img_color = ImageEnhance.Color(img1)
img_b = img_color.enhance(2)
img_output.paste(img_b,(w,0))

imgc = img_color.enhance(0.1)
img_output.paste(imgc,(2*w,0))


img_output.show()
