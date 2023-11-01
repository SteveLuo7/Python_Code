for x in (20,30,40):
    print(x,end="")
for y in "abcdefg":
    print(y,end="")
print("**********************************************")
str = {"name":"Cristiano", "age":"38", "title":"GOAT"}
for x in str:
    print(x,end="\t")
for x in str.items():
    print(x,end="\t")
print("===============================================")
for x in str.values():
    print(x,end="")
for x in str.keys():
    print(x,end="\n")

for i in range(10):
    print(i)

sum_all = 0
sum_dan = 0
sum_shuang = 0
for a in range(101):
    sum_all += a
    if a %2 == 0:
        sum_shuang += a
    else:
        sum_dan += a
print("0-100总数为{}，单数相加为{},偶数相加为{}".format(sum_all,sum_dan,sum_shuang))
