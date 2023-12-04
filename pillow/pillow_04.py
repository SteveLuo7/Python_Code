'''
    eval thumbnail
'''

from PIL import Image

img1 = Image.open('bjsxt.png')
# img1.show()
#
# #   eval every pixel 2 size
# Image.eval(img1,lambda x:x*2).show()
#

#   eval with size
img2 = img1.copy()
print(img2.size)

img2.thumbnail((200,160))
img2.show()
print(img2.size)