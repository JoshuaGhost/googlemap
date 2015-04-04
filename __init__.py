from flask import Flask
from randstr import *

def register_blueprints (app):
	from googlemap.views import posts
	app.register_blueprint(posts)

app = Flask(__name__)
app.config["SECRET_KEY"] = str([i for i in random_string(16)])


register_blueprints(app)

if __name__ == "__main__":
	app.run()
