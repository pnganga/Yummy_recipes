import flask
import unittest
from flask_testing import TestCase
from app import app
from app import simulated_models


class TestYummyRecipes(TestCase):

	# testing if routes render the right templates	
	def create_app(self):
		return  app

	def test_root(self):
		self.client.get('/')
		self.assert_template_used('index.html')

	def test_register(self):
		self.client.get('/register')
		self.assert_template_used('register.html')

	def test_login(self):
		self.client.get('/login')
		self.assert_template_used('login.html')


	# testing User object, that creates a users
	def test_user_gets_created(self):
		self.user = simulated_models.User(1, "Pius", "Ngash", "pnganga05@gmail.com", "585865", "password")
		self.assertEqual(self.user.user_details, {"id": 1,"firstname": "Pius", "lastname": "Ngash", "email": "pnganga05@gmail.com", "mobilenumber": "585865", "password": "password"})
		
	# testing Users object for storing Users
	def test_users_object_is__initially_empty(self):
		self.users = simulated_models.Users()
		self.assertEqual(simulated_models.users_db, []) 
	

	def test_users_get_returned(self):
		self.users = simulated_models.Users()
		self.assertEqual(self.users.get_all_users(), self.users.users)

		






    
