with open(r"123.txt","r") as f:
    str = f.readline()
    print("FileName {}".format(f.name))
    print("File Postion {}".format(f.tell()))
    print("==================")
    print("FileInformation {}".format(str))
    print("File Postion {}".format(f.tell()))
