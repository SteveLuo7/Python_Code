from PIL import Image

img1 = Image.open('blend1.jpg')
img2 = Image.open('blend2.jpg')
#   same size
img2 = img2.resize(img1.size)
#   spilt
r1,g1,b1 = img1.split()
r2,g2,b2 = img2.split()

temp = [r1,g2,b1]
img = Image.merge('RGB',temp)
img.show()



