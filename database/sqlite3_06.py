import sqlite3

con = sqlite3.connect('D:/sqlite3Demo/demo.db')

cur = con.cursor()

try:
    update_sql = "update t_person set pname=? where pno=?"
    cur.execute(update_sql,('steve',1))

    con.commit()
    print('MODIFIED SUCCESS')
except Exception as e:
    con.rollback()
    print(e)
    print('MODIFIED FAILED')
finally:
    cur.close()
    con.close()