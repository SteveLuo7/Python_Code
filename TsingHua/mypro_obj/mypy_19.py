try:
    f = open(r"123.txt","w")
    str = "Luoshibin"
    f.write(str)
except BaseException as e:
    print(e)
finally:
    f.close()
    print("END THE APP")
    