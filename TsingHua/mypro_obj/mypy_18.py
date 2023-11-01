try:
    f = open("d:/123.txt")
    content = f.readline()
    print(content)

except:
    print("File Not Found 404")
finally:
    print("run in finally")
    try:
        f.close()
    except BaseException as e:
        print(e)
print("END THIS APP")