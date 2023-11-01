for i in [1,2,3]:
    print(i)

names = ('cristiano','messi','neymar','suarez')
ages = (18,23,24,25)
jobs = ('teacher','footballler','actor','trash')

for names,ages,jobs in zip(names,ages,jobs):
    print("{}-{}-{}".format(names,ages,jobs))

# for i in range(3):
#     print("{}--{}--{}".format(names[i],jobs[i],ages[i]))