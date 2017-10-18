from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
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


    