'''
    filter
'''

from PIL import Image,ImageFilter

img = Image.open('lena.jpg')
w,h = img.size

#   create a new picture
img_output = Image.new('RGB',(2*w,h))
img_output.paste(img,(0,0))


filters = []
img_filter1 = img.filter(ImageFilter.GaussianBlur)
img_filter2 = img.filter(ImageFilter.FIND_EDGES)
img_filter3 = img.filter(ImageFilter.EDGE_ENHANCE)
filters.append(img_filter1)
filters.append(img_filter2)
filters.append(img_filter3)

for img_filter in filters:
    img_output.paste(img_filter,(w,0))
    img_output.show()

