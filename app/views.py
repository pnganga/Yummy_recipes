from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm, SignUpForm

users = []
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
			user = {"firstname": form.firstname.data,
					"lastname": form.lastname.data,

					}
			users.append(user)
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
    
