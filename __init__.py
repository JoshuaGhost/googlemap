from flask import Flask
from flask.ext.mongoengine import MongoEngine
from randstr import *

def register_blueprints (app):
	from googlemap.views import posts
	app.register_blueprint(posts)

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "googlemap"}
app.config["SECRET_KEY"] = str([i for i in random_string(16)])

db = MongoEngine(app)

register_blueprints(app)

if __name__ == "__main__":
	app.run()
