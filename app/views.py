from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm, SignUpForm
from simulated_models import User, Users


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = SignUpForm()
	if request.method == 'GET':
		return render_template('register.html', form = form)
	elif request.method == 'POST':
		if form.validate_on_submit():
			users_available = Users.get_all_users()
			user = Users((len(users_available)+1),form.firstname.data, form.lastname.data, form.email.data, form.mobilenumber.data, ).user_details()
			Users.add_user(Users)
			return redirect('login')
		else:
			return render_template('register.html', form = form)


@app.route('/user-recipes')
def user_recipes():
	return render_template('user-recipes.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
    
