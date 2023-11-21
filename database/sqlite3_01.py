'''
导入sqlite3 模块
创建链接 sqlite3.connect()


'''
import sqlite3
#   创建链接
con = sqlite3.connect('D:/sqlite3Demo/demo.db')
#   创建游标指针
cur = con.cursor()
#   编写制表sql语句
sql = '''create table t_person(
        pno INTEGER primary key autoincrement,
        pname VARCHAR not null,
        age INTEGER
        )'''
#   执行sql语句
try:
    cur.execute(sql)
    print("CREATE TABLE SUCCESS")
except Exception as e:
    print(e)
    print("CREATE TABLE FAILED")
finally:
    cur.close()
    con.close()


