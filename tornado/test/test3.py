import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates/login.html')

class LoginHandler(tornado.web.RequestHandler):
    def post(self,*args,**kwargs):
        uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')
        favs = self.get_arguments('fav')

        if uname == 'zhangsan' and pwd == '1234':
            self.write('Login Success')
        else:
            self.write('Login Fail')

app = tornado.web.Application([
    (r"/",IndexHandler),
    (r"/login/",LoginHandler),
])

app.listen(8000)

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().start()
