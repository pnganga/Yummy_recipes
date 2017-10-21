from flask import render_template, flash, redirect, request, session
from app import app
from .forms import LoginForm, SignUpForm, NewRecipeForm
import simulated_models 
from app.ensure_loggedin import ensure_logged_in


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

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'GET':
		return render_template('login.html', form = form)
	elif request.method == 'POST':
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


@app.route('/user-recipes')
@ensure_logged_in
def user_recipes():
	users = simulated_models.Users()
	my_user = {}
	for user in users.get_all_users():
		if session["logged_in"] in user["email"]:
			my_user = user
		else:
			return redirect('register')
	recipes = simulated_models.Recipes(session["logged_in"])
	my_recipes = recipes.fetch_user_recipes()
	return render_template('user-recipes.html', user_is_logged_in = True, user = my_user, recipes = my_recipes)


@app.route('/new_recipe', methods = ['GET', 'POST'])
@ensure_logged_in
def new_recipe():
	form = NewRecipeForm()
	users = simulated_models.Users()
	my_user = {}
	for user in users.get_all_users():
		if session["logged_in"] in user["email"]:
			my_user = user
	if request.method == 'GET':
		return render_template('new-recipe.html', form = form, user_is_logged_in = True, user = my_user)
	elif request.method == 'POST':
		if form.validate_on_submit():
			# adding a recipe to db
			recipes = simulated_models.Recipes(session["logged_in"])
			recipes_available = recipes.all_recipes
			recipe = simulated_models.Recipe((len(recipes_available)+1),form.name.data, form.content.data, form.category.data, session["logged_in"])
			recipes.add_recipe(recipe)
			# adding recipe category automatically
			recipe_categories = simulated_models.RecipeCategorys(session["logged_in"])
			recipe_categories_available = recipe_categories.all_recipe_categories
			recipe_category = simulated_models.RecipeCategory((len(recipe_categories_available)+1),form.category.data, session["logged_in"])
			recipe_categories.add_recipe_category(recipe_category)
			print 
			return redirect('user-recipes')
		else:
			return render_template('register.html', form = form)

@app.route('/new_recipe_category', methods = ['GET', 'POST'])
@ensure_logged_in
def new_recipe_category():
	users = simulated_models.Users()
	my_user = {}
	for user in users.get_all_users():
		if session["logged_in"] in user["email"]:
			my_user = user
	return render_template('new_recipe_category.html', user_is_logged_in = True, user = my_user)
	
    
