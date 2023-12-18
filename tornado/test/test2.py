'''
    login function with tornado
'''

import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates/login.html')


class LoginHandler(tornado.web.RequestHandler):
    # def get(self,*args,**kwargs):
    #     uname = self.get_query_argument('uname')
    #     pwd = self.get_query_argument('pwd')
    #     favs = self.get_query_arguments('fav')
    #     self.write('%s,%s,%s'%(uname,pwd,favs))


    def post(self,*args,**kwargs):
        uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')
        favs = self.get_arguments('fav')

        self.write('%s,%s,%s'%(uname,pwd,favs))




app = tornado.web.Application([
    (r'/',IndexHandler),
    (r'/login/',LoginHandler),
])

if __name__ == '__main__':

    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()