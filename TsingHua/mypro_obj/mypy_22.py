# a = ["Cristiano","Messi\n","Benzema\n"]
# b = enumerate(a)
# print(a)
# print(list(b))

with open (r"123.txt","r") as f:
    lines = f.readlines()
    lines = [temp.rstrip()+" #"+str(index)for index,temp in enumerate(lines)]

with open(r"123.txt","w") as f:
    f.writelines(lines)