#   导入pymysql模块
import pymysql
#   创建链接
con = pymysql.connect(host='localhost',user='root',password='root',database='python_db',port=3306)

#   创建游标对象
cur = con.cursor()
#   database sql
sql = '''
        create table t_student(
            sno int primary key auto_increment,
            sname varchar(30) not null ,
            age int(2),
            score float(3,1)
        )
'''
#   执行表的sql
try:
    cur.execute(sql)
    print('Create Table Success')
except Exception as e:
    print(e)
    print('Create Table failed')
finally:
    cur.close()
    con.close()