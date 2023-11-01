print('step0')
try:
    print("step1")
    a = 3/1
    print("step2")
except BaseException as e:
    print("step3")
    print(e)

    # print("Exception, Zero cant be division")
print("===============")