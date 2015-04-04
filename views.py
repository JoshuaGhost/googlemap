from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form

posts = Blueprint('posts', __name__, template_folder='templates')

class TestView(MethodView):

	def get(self):
		return render_template('test/test.html', posts = posts)
		
posts.add_url_rule('/', view_func = TestView.as_view('test'))