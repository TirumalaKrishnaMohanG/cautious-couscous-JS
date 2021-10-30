##################################
# Copyright						 #
# Name: Tirumala Krishna Mohan G #
# Assignment : URL Shorten       #
##################################

#!/usr/bin/env python

# Headers
import re
import requests
import pandas as pd
import MySQLdb.cursors
from flask import Flask
from flask import flash
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from datetime import datetime
from flask_mysqldb import MySQL
from flask_session import Session
from flask import render_template
from flask_shorturl import ShortUrl

 
# Creating Flask App
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1226'
app.config['MYSQL_DB'] = 'karthik_assignment'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'this should be a secret random string'
Session(app)

su = ShortUrl(app)

# MySQL App
mysql = MySQL(app)

# Base Page {Login}
@app.route('/')
@app.route('/login',methods=['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM users WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
		    session['loggedin'] = True
		    session['id'] = account['pid']
		    session['username'] = account['username']
		    msg = 'Logged in successfully !'
		    return redirect(url_for('home'))
		elif account and len(account) > 9:
			msg = 'Userlenght is exceeded,Choose the length of your account between 9 and less'
			return render_template('Login.html', msg = msg)
		else:
		    msg = 'Incorrect username / password !'
	return render_template('Login.html', msg = msg)

# Register Page 
@app.route('/register', methods =['GET', 'POST'])
def register():
	try:
		msg = ''
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		    username = request.form['username']
		    password = request.form['password']
		    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		    cursor.execute('SELECT * FROM users WHERE username = % s', (username, ))
		    account = cursor.fetchone()
		    if account:
		        msg = 'Account already exists !'
		    elif not re.match(r'[A-Za-z0-9]+', username):
		        msg = 'User must fill the form'
		    elif not username or not password:
		        msg = 'Please fill out the form !'
		    else:
		        cursor.execute('INSERT INTO users VALUES (NULL, % s, % s)', (username, password, ))
		        mysql.connection.commit()
		        msg = 'You have successfully registered !'
		elif request.method == 'POST':
		    msg = 'Please fill out the form !'
	except:
		msg = 'Userlenght is exceeded,Choose the length of your account between 9 and less'
	return render_template('register.html', msg = msg)

# Home Page
@app.route('/home',methods=['GET', 'POST'])
def home():
	if not session.get('username'):
		return redirect('/')
	else:
		return render_template('index.html')

# Shorten the URL
@app.route('/result',methods=['GET', 'POST'])
def result():
	if not session.get('username'):
		return redirect('/')
	else:
		status =  ''
		if request.method == 'POST':
			getURL = request.form['url']
			print(getURL)
			getInfo = requests.get(getURL,verify=False,allow_redirects=False).status_code
			try:
				hashid = su.encode_url(len(getURL))
				status = request.host_url + hashid
				currDT = datetime.now().strftime('%Y-%m-%d %H:%M')
				cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
				cursor.execute('INSERT INTO urls VALUES (NULL, %s, % s, % s, %s)', (hashid, getURL, status, currDT))
				mysql.connection.commit()				
			except:
				status = "Url is invalid"
		return render_template('index.html',msg=status)


# Redirect the URL
@app.route('/forwordurl/<id>',methods=['GET', 'POST'])
def forwordurl(id):
	if not session.get('username'):
		return redirect('/')
	else:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM urls WHERE uid = % s', (id, ))
		getInfo = cursor.fetchone()
		getPreviousUrl = getInfo.get('previousurl')
		return redirect(getPreviousUrl)


# History Page
@app.route('/history',methods=['GET', 'POST'])
def history():
	if not session.get('username'):
		return redirect('/')
	else:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		status = cursor.execute('SELECT * FROM urls')
		account = cursor.fetchall()
		get_INFO = [{'pid':x.get('pid'),'previousurl':x.get('previousurl'),'originalurl':x.get('originalurl'),'date':x.get('date')} for x in account]
		return render_template("history.html",status=account)

# Logout Page
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))