'''
    inquire data from database by pymysql
'''

#   导入pymysql模块
import pymysql
#   创建链接
con = pymysql.connect(host='localhost',user='root',password='root',database='python_db',port=3306)
#   创建游标对象
cur = con.cursor()
#   database sql
sql = '''
      select * from t_student
'''
#   执行表的sql
try:
    cur.execute(sql)
    student = cur.fetchone()
    sno = student[0]
    sname = student[1]
    age = student[2]
    score = student[3]
    print('sno:', sno,
          'sname:', sname,
          'age:', age,
          'score:', score)
except Exception as e:
    print(e)
    con.rollback()
    print('Search Data Failed')
finally:
    cur.close()
    con.close()