from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def user_login():

    username = request.form['username']
    password = request.form['password']
    pwd = request.form['pwd']

    username_error = ''
    password_error = ''
    verification_error = ''

#def username():
    if len(username) == 0:
        username_error = 'Nothing has been put in'
        username = ''
    elif ' ' in username:
        username_error = 'Can not have a space'
        username = ''
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Incorrect number of characters'
        username = ''

#def password():
    if len(password) == 0:
        password_error = 'Nothing has been put in'
        password = ''
    elif ' ' in password:
        password_error = 'Can not have a space'
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Incorrect number of characters'
        password = ''

#def pwd():
    if pwd != password:
        verification_error = 'Passwords do not match'
        pwd = ''
    elif len(pwd) == 0:
        verification_error = 'Nothing has been put in'
        pwd = ''

#def welcome():
    if not username_error and not password_error and not verification_error:
        username = request.form['username']
        return render_template('welcome.html', name=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, verification_error=verification_error, username=username, password=password, pwd=pwd)


app.run()
    
