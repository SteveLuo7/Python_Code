from PIL import Image

#   open picture

img = Image.open('img.png')

#   display
# img.show()

print('Picutres format: ',img.format)
print('Picutres size: ',img.size)
print('Picutres height: ',img.height)
print('Picutres width: ',img.width)
print('get(100,100) pixels: ',img.getpixel((100,100)))

