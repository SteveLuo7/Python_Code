from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import text

app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'database_learn'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

db = SQLAlchemy(app)

migrate = Migrate(app,db)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text('select 1'))
#         print(rs.fetchone())

class User(db.Model):
    __tablename__ ='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100))
    signature = db.Column(db.String(100))

# user = User(username='root', password='root')


class Artcle(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref='articles')



# user = User.query.get(article.author_id)

# with app.app_context():
#     db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/user/add')
def add_user():
    #   create orm object
    user1 = User(username='steve',password='1234')
    user2 = User(username='luo',password='1234')
    user3 = User(username='zhu',password='1234')

    #   add to db.session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    #   db.session commit
    db.session.commit()
    return "USER CREATED SUCCESSFUL"


@app.route('/user/query')
def user_query():
    # user = User.query.get(1)
    # print(f"{user.id}:{user.username}-{user.password}")
    users = User.query.filter_by(username='steve')
    for user in users:
        print(user.username)

    return 'USER QUERY SUCCESSFUL'

@app.route('/user/update')
def user_update():
    user = User.query.filter_by(username='steve').first()
    user.password = '1111111'
    db.session.commit()
    return 'USERDATA MODIFIED SUCCESSFUL'

@app.route('/user/delete')
def user_delete():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
    return 'USER DELETED SUCCESSFUL'


@app.route('/article/add')
def article_add():
    article1 = Artcle(title='Flask Learning Lesson', content='FlaskXXXXXXXXXXXXXXXXXXXXX')
    article1.author = User.query.get(2)

    article2 = Artcle(title='Django Learning Lesson', content='DjangoXXXXXXXXXXXXXXXXXXXXX')
    article2.author = User.query.get(2)

    db.session.add_all([article1,article2])
    db.session.commit()

    return 'Article has been added'

@app.route('/article/query')
def article_query():
    user = User.query.get(2)
    for article in user.articles:
        print(article.title)
    return "Article your enquire has finished"

if __name__ == '__main__':
    app.run()
