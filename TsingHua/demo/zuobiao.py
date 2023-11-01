x = int(input(""))
y = int(input(""))
str = ""
if x ==0 and y == 0 :
    str = "坐标在原点"
elif x == 0:
    str = "坐标在X轴上"
elif y == 0:
    str = "坐标在Y轴上"
elif x > 0 and y > 0 :
    str = "坐标在第一象限"
elif x > 0 and y < 0 :
    str = "坐标在第二象限"
elif x < 0 and y < 0 :
    str = "坐标在第三象限"
else:
    str = "坐标在第四象限"

print("坐标为{}{},坐标位于{}".format(x,y,str))