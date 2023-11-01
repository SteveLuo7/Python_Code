p = input("学生的分数")
g = ""
if int(p) <60:
    g = "不及格"
elif int(p) < 79:
    g = "良好"
elif int(p) > 79:
    g = "优秀"

print("分数是{0},成绩是{1}".format(p,g))