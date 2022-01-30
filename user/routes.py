from app import app
from user.modules import signup


@app.route('/user/signup', methods=['GET'])
def signup():
    return signup()
