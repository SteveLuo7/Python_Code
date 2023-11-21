
'''
查询sqlite3
导入模块
创建链接
输入查询语句
获取
fetchall（）
遍历

'''

import sqlite3

con = sqlite3.connect('D:/sqlite3Demo/demo.db')

cur = con.cursor()

sql = 'select * from t_person'
try:
    cur.execute(sql)
    #   获取结果集
    person = cur.fetchone()
    print(person)
except Exception as e:
    print(e)
    print('SEARCH FAILED')
finally:
    cur.close()
    con.close()