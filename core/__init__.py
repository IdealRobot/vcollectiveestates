from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # 🔑 DATABASE CONFIG
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://suffermedaily:CollectiveEstateSQL123%24%25%5E@suffermedaily.mysql.pythonanywhere-services.com/suffermedaily$collective_estate'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 🔌 INIT DB
    db.init_app(app)

    return app