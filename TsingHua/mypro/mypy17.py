def outer():
    print('outer is running...')

    def inner():
        print('inner is running')
    inner()
outer()


print("*************")

def printChineseName(Name,FamilyName):
    print("{}{}".format(FamilyName,Name))
def printEnglishName(Name,FamilyName):
    print("{}{}".format(Name,FamilyName))

def printName(isChinese,Name,FamilyName):
    def inner_print(a,b):
        print("{}{}".format(a,b))

    if isChinese:
        inner_print(FamilyName,Name)
    else:
        inner_print(Name,FamilyName)

printName(True,'shibin','Luo')