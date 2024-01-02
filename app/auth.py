from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from urllib.parse import unquote
from .connect_db import check, insert

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    check_login = check("select * from users where username = ? and password = ?", (username,password))
    if check_login:
        print("login fail")
        return redirect(url_for('views.login'))
    else:
        print("login success")
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
    print(username)
    check_username = check("select * from users where username = ?", (username,))
    if check_username:
        print("username not exists")
        insert("insert into users (username, password) values (?, ?)", (username, password))
        return redirect(url_for('views.home'))
    else:
        print("username exists")
        return redirect(url_for('views.home'))

    
    

