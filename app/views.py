from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/user-recipes')
def user_recipes():
	return render_template('user-recipes.html')

@app.route('/login', methods = ["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' % (form.email.data, str(form.password.data)))
        # return redirect('/user-recipes')
	return render_template('login.html', form = form)