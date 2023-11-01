import time

start = time.time()

for i in range(1000):
    result =[]
    for m in range(10000):
        result.append(1*1000+m*100)
end = time.time()

print("总耗时{}".format(end-start))

start2 = time.time()

for x in range(1000):
    result=[]
    c = x * 1000
    for y in range(10000):
        result.append((x+y*100))
end2 = time.time()

print("2总耗时{}".format(end2-start2))