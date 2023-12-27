import random
import string

from flask import Blueprint, render_template, jsonify
from exts import mail, db
from flask_mail import Message
from flask import request
import _string
from models import EmailCaptchaModel

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/register")
def register():
    return render_template("register.html")

@bp.route("/mail/test")
def mail_test():
    message = Message(
        subject="MAIL TEST",
        recipients=["Luoshibin950104@outlook.com"],
        body="THIS IS A EMAIL TEST"
    )
    mail.send(message)
    return "MAIL HAS BEEN SENT SUCCESSFUL"

@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    print(captcha)

    message = Message(
        subject="XIAOLUO EMAIL TEST",
        recipients=["Luoshibin950104@outlook.com"],
        body="YOUR SERVICE CODE IS : {}".format(captcha)
    )
    mail.send(message)

    #   memcached // redis
    #   database
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    #   RESTful API
    #   {code: 200/400/500, message: "", data: {}}
    return jsonify({"code": 200, "message": "", "data": None})
