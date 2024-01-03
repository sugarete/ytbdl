from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from urllib.parse import unquote
from .connect_db import check, insert

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    check_login = check("select * from users where username = ? and password = ?", (username,password))
    if check_login:
        print("Password or username is incorrect")
        return redirect(url_for('views.home'))
    else:
        flash("Login successful")
        session['username'] = username
        return redirect(url_for('views.home'))

@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('views.home'))

@auth.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    retype_password = request.form.get('confirm_password')
    if password != retype_password:
        print("password not match")
        return redirect(url_for('views.home'))
    print(username)
    check_username = check("select * from users where username = ?", (username,))
    if check_username:
        print("username not exists")
        insert("insert into users (username, password) values (?, ?)", (username, password))
        return redirect(url_for('views.home'))
    else:
        print("username exists")
        return redirect(url_for('views.home'))

    
    

