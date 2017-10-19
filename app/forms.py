from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextareaField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

class SignUpForm(FlaskForm):
	firstname = StringField('firstname', validators=[DataRequired()])
	lastname = StringField('lastname', validators=[DataRequired()])
	mobilenumber = StringField('mobilenumber', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired(), Email()])
	password = PasswordField('password', validators=[DataRequired()])
	password2 = PasswordField('password2', validators=[DataRequired()])

class NewRecipeForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	content = StringField('contentname', validators=[DataRequired()])
	category = StringField('category', validators=[DataRequired()])
	


    