'''
    use pymysql insert several data
'''

#   导入pymysql模块
import pymysql
#   创建链接
con = pymysql.connect(host='localhost',user='root',password='root',database='python_db',port=3306)
#   创建游标对象
cur = con.cursor()
#   database sql
sql = '''
       insert into t_student(
            sname,age,score
       ) values (%s,%s,%s)
'''
#   执行表的sql
try:
    cur.executemany(sql,[('steve',29,9.5),('Cristiano',38,10.0),('benzema',29,9.0),('pessi',35,0.0)])
    con.commit()
    print('Insert Data Success')
except Exception as e:
    print(e)
    con.rollback()
    print('Insert Data Failed')
finally:
    cur.close()
    con.close()