import sqlite3

con = sqlite3.connect('D:/sqlite3Demo/demo.db')

cur = con.cursor()

try:
    #   delete sql
    update_sql = "delete from t_person where pno=?"
    #   parameter must be tuple
    cur.execute(update_sql,(1,))

    con.commit()
    print('DELETE SUCCESS')
except Exception as e:
    con.rollback()
    print(e)
    print('DELETE FAILED')
finally:
    cur.close()
    con.close()