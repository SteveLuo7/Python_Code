import os
all_files = []
path = os.getcwd()
list_files = os.walk(path)

for dirpath,dirname,filename in list_files:
    for dir in dirname:
        print(os.path.join(dirpath,dir))
        all_files.append(os.path.join(dirpath,dir))
    for file in filename:
        all_files.append(os.path.join(dirpath,file))


for file in all_files:
    print(file)