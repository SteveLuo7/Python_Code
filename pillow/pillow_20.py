from PIL import Image
import numpy as np
import os
import pickle
#   read picture from Images folder
image_dir = './images/'
result_dir = './result/'

array_file = './array.bin'
def image_to_array_file():
    file_name = os.listdir(image_dir)
    # print(file_name)
    #   travel all the file from folder
    #   generate a element to save array includes 8 pic
    image_arrs = np.array([])
    for filename in file_name:
        img = Image.open(image_dir+filename)
        #   split every single picture
        r,g,b = img.split()

        r_arr = np.array(r).reshape(62500)
        g_arr = np.array(g).reshape(-1)
        b_arr = np.array(b).reshape(62500)

        #   spilt to array with r_arr, g_arr, b_arr
        arrs = np.concatenate((r_arr,g_arr,b_arr))
        image_arrs = np.concatenate((arrs,image_arrs))

        # print(image_arrs.shape)
    #   save this array
    with open(array_file,'wb') as f:
        pickle.dump(image_arrs,f)

#   read file , transfer to pic

def file_to_image():
    with open(array_file,'rb') as f:
        images = pickle.load(f)
        #   array 8,3,250,250
        image_arr = images.reshape((8,3,250,250))

    for i in range(8):
        r = Image.fromarray(image_arr[i][0]).convert('L')
        g = Image.fromarray(image_arr[i][1]).convert('L')
        b = Image.fromarray(image_arr[i][2]).convert('L')

        image = Image.merge('RGB',(r,g,b))
        image.save(result_dir+str(i)+'.jpg')

if __name__ == '__main__':
    # image_to_array_file()
    file_to_image()