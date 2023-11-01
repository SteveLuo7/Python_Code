import os 
import os.path
# os.system("ping www.baidu.com")

# os.system("console")

print(os.name)
print(os.sep)
print(os.linesep.__repr__())

print(os.getcwd())

print("----------------------------------")

print(os.path.isabs("123.txt"))
print(os.path.isdir("123.txt"))
print(os.path.isfile("123.txt"))
print(os.path.exists("123.txt"))

print(os.path.getsize("123.txt"))
print(os.path.abspath("123.txt"))
print(os.path.dirname("123.txt"))
print(os.path.getatime("123.txt"))
print(os.path.getctime("123.txt"))
print(os.path.getmtime("123.txt"))




