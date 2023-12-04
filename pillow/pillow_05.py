'''
    Cut and Paste
'''

from PIL import Image
img = Image.open('bjsxt.png')

imgb = img.copy()
imgc = img.copy()

#   cut
img_crop = imgb.crop((10,10,120,120))
#   paste
imgc.paste(img_crop,(20,20))
imgc.show()