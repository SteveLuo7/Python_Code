try:
    a = input("输入一个被除数")
    b = input("输入一个除数")
    c = float(a)/float(b)
except BaseException as e:
    print("数据错误")
    print(e)
else:
    print(c)
finally:
    print("计算程序结束")