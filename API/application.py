from flask import Flask
import mysql.connector
app = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)

# class Drink(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     description = db.Column(db.String(120))

#     def __repr__(self, name, description):
#         self.name = name
#         self.description = description

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    # drinks = Drink.query.all()

    # output = []
    # for drink in drinks:
    #     drink_data = {'name': drink.name, 'description': drink.description}
    #     output.append(drink_data)
    return {"drinks": 'drinks'}