import os.path

import MySQLdb
import tornado.ioloop
import tornado.web

def _getConn():
    return MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='test9_db',port=3306)
class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('templates/register.html')

class RegisterHandler(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')

        cursor = self.conn.cursor()
        cursor.excute('insert into t_user values(null,"%s","%s",now())'%(username,password))

        self.conn.comit()
        # Perform validation on username and password if needed
        # ...

        # In a real-world scenario, you should hash the password before storing it
        # For simplicity, this example does not include password hashing.

        # Here, you can save the user information to a database or perform any other necessary actions.
        # For now, let's just print the received data.
        print(f"Username: {username}, Password: {password}")

        self.write(f"Registration successful for {username}")

app = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/register/", RegisterHandler,{'conn':_getConn()}),
])

app.listen(8000)

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().start()
