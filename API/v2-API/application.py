from flask import Flask, request, jsonify
from db import my_db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/drinks')
def get_drinks():
    mycursor = my_db.cursor()
    sql = "SELECT * FROM drinks "
    mycursor.execute(sql)
    result = mycursor.fetchall()

    return {"Drinks": result}

@app.route('/get_drinks', methods=['GET'])
def get_drinks_sqlite():
    drink = Drinks.query.all()

    output = []
    for drink in drink:
        drint_data = {'id': drink.id, 'name': drink.name, 'description': drink.description}

        output.append(drint_data)

    return {'Drinks': output}

@app.route('/get_drinks/<id>', methods=['GET'])
def get_drinks_sql(id):
    drink = Drinks.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.description}

@app.route('/add_drinks', methods=['POST'])
def add_drinks():
    data = request.get_json()
    drink = Drinks(name=data['name'], description=data['description'])
    db.session.add(drink)
    db.session.commit()

    return jsonify({'id': drink.id})