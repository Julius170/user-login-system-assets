from app import app
from user.modules import signup


@app.route('/user/signup', methods=['POST']) 
def signup():
    return signup()