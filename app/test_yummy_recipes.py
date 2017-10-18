import flask
import unittest
from flask.ext.testing import TestCase
from app import app


class TestYummyRecipes(TestCase):
		
	def create_app(self):
		return  app
		
	def test_root(self):
		self.client.get('/')
		self.assert_template_used('index.html')

	def test_register(self):
		self.client.get('/register')
		self.assert_template_used('register.html')

	def test_register(self):
		self.client.get('/login')
		self.assert_template_used('login.html')
		




    
