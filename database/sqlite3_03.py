#   导入模块
import sqlite3
#   创建链接
con = sqlite3.connect('D:/sqlite3Demo/demo.db')
#   创建游标指针
cur = con.cursor()
#   插入sql修改语句
sql = "insert into t_person(pname,age) values (?,?)"
#   执行sql语句
try:
    cur.executemany(sql,[("CRISTIANO",38),("KOBE",37)])
    con.commit()
    print("MODIFY SEVERAL DATA SUCCESS")
except Exception as e:
    print(e)
    con.rollback()
    print("MODIFY SEVERAL DATA FAILED")
finally:
    cur.close()
    con.close()