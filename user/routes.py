from flask import Flask
from user.modles import User
from app import app


@app.route('/user/signup', methods=["POST"])
def signup():
    return User().signup()




