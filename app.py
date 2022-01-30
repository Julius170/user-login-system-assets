from flask import Flask, render_template

# if  __name__ == "__main__":
#     app.run(debug= True) 

app = Flask(__name__)

# ROUTES
from user import routes


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
