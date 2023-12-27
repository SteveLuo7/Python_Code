from flask import Flask, render_template

app = Flask(__name__)


class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

@app.route('/')
def hello_world():  # put application's code here
    user = User(username='Steve',password='1234')
    person = {
        'username': 'luoshibin',
        'email' : "291581211@qq.com"
    }
    return render_template('index.html',user=user,person=person)

@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template('blog_detail.html',blog_id=blog_id)

@app.route('/filter')
def filter_demo():
    user = User(username='zhu',password='1234')
    return render_template('filter.html',user=user)

@app.route('/control')
def control_statement():
    age = 17
    books = [
        {"name":"三国演义",
         "author":"罗贯中"},
        {"name":"水浒传",
         "author":"施耐庵"}
    ]
    return render_template('control.html',age=age,books=books)

@app.route('/child1')
def child():
    return render_template('child1.html')

@app.route('/child2')
def child2():
    return render_template('child2.html')

@app.route('/static')
def static_demo():
    return render_template('static.html')

if __name__ == '__main__':
    app.run()
