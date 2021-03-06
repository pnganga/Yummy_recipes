# These are lists that acts as dbs for storing users, recipes and recipe categories
users_db = []
recipe_db = []
recipe_category_db = []

# catching errors

class UserNotFoundException(Exception):
    pass


class NullUserError(Exception):
    pass


class RecipeNotFoundError(Exception):
    pass

# this is a class for handling adding and retrieving users from the users list

class Users():
    def __init__(self):
        self.users = users_db

    def add_user(self, user):
        if user:
            if len(self.users) == 0:
                self.users.append(user.user_details)
            else:
                for u in self.users:
                    if u["email"] == user.email:
                        raise NullUserError("user already exists") 
                    else:
                        self.users.append(user.user_details) 
        else:
            raise NullUserError("Cannot add empty user")

    def get_all_users(self):
        return self.users

# this class is responsible for creating a new user given form inputs

class User():
    def __init__(self, id, firstname, lastname, email, mobilenumber, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobilenumber = mobilenumber
        self.password = password

    @property
    def user_details(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "mobilenumber": self.mobilenumber,
            "password": self.password
        }

    def __repr__(self):
        return "<User %s %s>".format(self.firstname, self.lastname)

# This class is responsible for creating a new recipe from the user inputs


# This  class handles logic for adding, retrieving, editing and deleting recipes

class Recipes():
    def __init__(self, user_email):
        self.recipes = self.__get_user_recipes(user_email)
        self.all_recipes = recipe_db

    def __get_user_recipes(self, user_email):
        user_recipes = []
        for recipe in recipe_db:
            if user_email in recipe["owner"]:
                user_recipes.append(recipe)
            else:
                return recipe_db
        return user_recipes

    def add_recipe(self, recipe):
        if recipe:

            self.all_recipes.append(recipe.recipe_details) 
        else:
            raise NullUserError("Cannot add empty recipe")


    def edit_recipe(self, recipe_id, new_recipe):
        for recipe in recipe_db:
            if int(recipe_id) == int(recipe["id"]):
                recipe_db[recipe_db.index(recipe)] = new_recipe.recipe_details
            else:
                raise RecipeNotFoundError("Recipe Not found")


    def delete_recipe(self, recipe_id):
        for recipe in recipe_db:
            if int(recipe_id) == int(recipe["id"]):
                del(recipe_db[recipe_db.index(recipe)])
            else:
                raise RecipeNotFoundError("Recipe Not found")
        
    def view_recipe(self, recipe_id):
        recipe = {}
        for rec in self.recipes:
          
            if int(recipe_id) == int(rec["id"]):    
               recipe = rec
            else:
               pass
        return recipe

    def fetch_user_recipes(self):
        return self.recipes

class Recipe():
    def __init__(self, id, name, content, category, owner):
        self.id = id
        self.name = name
        self.content = content
        self.category = category
        self.owner = owner
    @property
    def recipe_details(self):
        return {
            "id":  self.id,
            "name": self.name,
            "content": self.content,
            "category": self.category,
            "owner": self.owner
        }

    def __repr__(self):
        return "<Recipe %s>".format(self.name)
# This class is responsible for creating a new recipe category from the user inputs

class RecipeCategory():
    def __init__(self, recipe_id, name, owner):
        self.id = recipe_id
        self.name = name
        self.owner = owner
    
    @property
    def recipe_category_details(self):
        return {
            "id": self.owner,
            "name": self.name,
            "owner": self.owner
        }

    def __repr__(self):
        return "<RecipeCategory %s>".format(self.name)

# This  class handles logic for adding, retrieving, editing and deleting recipe categories

class RecipeCategorys():
    def __init__(self, user_email):
        self.recipe_categories = self.__get_user_recipe_categories(user_email)
        self.all_recipe_categories = recipe_category_db

    def __get_user_recipe_categories(self, user_email):
        user_recipe_categories = []
        recipe_categories = recipe_category_db
        for recipe_category in recipe_categories:
            if user_email in recipe_category["owner"]:
                user_recipe_categories.append(recipe_category)
            
        return user_recipe_categories

    def add_recipe_category(self, recipe_category):
        if recipe_category:
            if len(self.all_recipe_categories) == 0:
                self.all_recipe_categories.append(recipe_category.recipe_category_details)
            else:
                
                self.all_recipe_categories.append(recipe_category.recipe_category_details) 
        else:
            raise NullUserError("Cannot add empty recipe category")


    def edit_recipe_category(self, user_email, recipe_category_id, new_recipe_category):
        for recipe_category in self.recipe_categories:
            if recipe_category_id in recipe_category["id"] and user_email in recipe_category["owner"]:
                recipe_category = new_recipe_category
            else:
                raise RecipeNotFoundError("Recipe category Not found")

    def fetch_user_recipe_categories(self):
        return self.recipe_categories
   
