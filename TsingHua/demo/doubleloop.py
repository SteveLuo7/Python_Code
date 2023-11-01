for m in range(1,10):
    for n in range(1,m+1):
        print("{}*{} = ".format(m,n), m*n,end="\t")
    print()


r1 = dict(name="cristiano",age=38,goal=40)
r2 = dict(name="haaland",age=24,goal=38)
r3 = dict(name="mbappe",age=25,goal=37)

tb = [r1,r2,r3]

for x in tb:
    if x.get("goal")>39:
        print(x.values())