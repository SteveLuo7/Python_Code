import shutil
import zipfile

# shutil.make_archive("/Users/steveluo/Documents/Python_Code/TsingHua/mypro","zip","/Users/steveluo/Documents/Python_Code/TsingHua/mypro")

# z1 = zipfile.ZipFile("123.zip","w")
# z1.write("123.txt")
# z1.close()

z2 = zipfile.ZipFile("123.zip","r")
z2.extractall("/Users/steveluo/Documents/Python_Code/TsingHua/mypro_obj")
z2.close()