with open(r"123.txt","r") as x:
    str = x.read()
    print(str)

    for a in x:
        print(a)

    x.close()