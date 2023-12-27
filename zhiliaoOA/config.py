#   setting database information

HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "zhiliaooa_course"
USERNAME = "root"
PASSWORD = "root"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


#   Setting Email
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "291581211@qq.com"
MAIL_PASSWORD = "awmtaksicrrtcabe"
MAIL_DEFAULT_SENDER = "291581211@qq.com"