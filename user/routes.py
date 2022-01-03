from flask import Flask
from app import app
from user.modules import User  



@app.route('/user/signup', methods=['POST']) 
def signup():
    return User().signup()