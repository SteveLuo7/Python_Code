import os.path

import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates/upload.html')

class UploadHandler(tornado.web.RequestHandler):
    def post(self,*args,**kwargs):
        img1 = self.request.files['img1']
        print(img1)

        for img in img1:
            body = img['body']
            content_type = img['content_type']
            filename = img['filename']

        with open(os.path.join(os.getcwd(),'files', filename),'wb') as fw:
            fw.write(body)

        self.set_header('Content-Type',content_type)
        self.write(body)


app = tornado.web.Application([
    (r"/",IndexHandler),
    (r"/upload/",UploadHandler),
])

app.listen(8000)

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().start()
