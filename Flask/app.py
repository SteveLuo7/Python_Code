
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'My name is SteveLuo'

@app.route('/profile')
def profile():
    return "This  is profile html"

@app.route("/blog/list")
def blog_list():
    return 'THIS IS BLOG LIST'

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return 'This is {}'.format(blog_id)

@app.route('/book/list')
def book_list():
    page = request.args.get("page",default=1, type=int)
    return 'THIS IS THE {} PAGE'.format(page+1)

if __name__ == '__main__':
    app.run()
