from flask import render_template, flash, redirect, request, session
from app import app
from .forms import LoginForm, SignUpForm
import simulated_models 


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
			users = simulated_models.Users()
			users_available = users.get_all_users()
			user = simulated_models.User((len(users_available)+1),form.firstname.data, form.lastname.data, form.email.data, form.mobilenumber.data, form.password.data )
			users.add_user(user)
			return redirect('/')
		else:
			return render_template('register.html', form = form)


@app.route('/user-recipes')
def user_recipes():
	users = simulated_models.Users()
	for user in users.get_all_users():
		if session["logged_in"] in user["email"]:
			my_user = user
			return render_template('user-recipes.html', user_is_logged_in = True, user = my_user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'GET':
		return render_template('login.html', form = form)
	elif request.method == 'POST':
		print "POST"
		users = simulated_models.Users()
		available_users = users.get_all_users()
		if available_users != []:
			for user in available_users:
				if form.email.data in user["email"] and user["password"] == form.password.data:
					session["logged_in"] = form.email.data
					
					return redirect('user-recipes')
				flash("Invalid username and password combination", "login_errors")
				return render_template('login.html', form=form)
		else:
			return redirect('register')

	
    
