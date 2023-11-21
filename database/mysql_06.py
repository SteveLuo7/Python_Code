'''
    update data from database by pymysql
'''

#   导入pymysql模块
import pymysql
#   创建链接
con = pymysql.connect(host='localhost',user='root',password='root',database='python_db',port=3306)
#   创建游标对象
cur = con.cursor()
#   database sql
sql = 'update t_student set sname=%s where sno=%s'

#   执行表的sql
try:
    cur.execute(sql,('chris',5))
    con.commit()
    print('Modified Data Success')

except Exception as e:
    print(e)
    con.rollback()
    print('Modified Data Failed')
finally:
    cur.close()
    con.close()