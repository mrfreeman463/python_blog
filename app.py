from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.database import db


# routes
from routes.web import web
from routes.api import api

app = Flask(__name__)

app.secret_key = "5mZWkax5n6szv"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:changeme@localhost:5432/python_blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(web)
app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_table():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)