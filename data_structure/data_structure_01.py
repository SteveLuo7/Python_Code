#   save information of a class
#   Information of class must be use the data_structure can save multiple data
#   students information:   sno,sname,age,score

#   tuple
stus= [
    ('1001','steve',23,99),
    ('1002','luo',24,96),
    ('1003','shi',25,97),
    ('1004','bin',26,98),
]

#   list
stus1 = [
    {'sno':'1001','sname':'steve','age':23,'score':99},
    {'sno':'1002','sname':'luo','age':24,'score':96},
    {'sno':'1003','sname':'shi','age':25,'score':97},
    {'sno':'1004','sname':'bin','age':26,'score':98},
]
#   if use list save students information , it must be use loop
for stu in stus1:
    print(stu)
print('------------------------------------------------')

#   dict
stus2 = {
    '1001':{'sname':'steve','age':23,'score':99},
    '1002':{'sname':'luo','age':24,'score':96},
    '1003':{'sname':'shi','age':25,'score':97},
    '1004':{'sname':'bin','age':26,'score':98},
}
#   if use dict save students information, it must use key get values
stu_dict1 = stus2['1002']
print(stu_dict1)
