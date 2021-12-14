from flask import Flask, request, jsonify, make_response
# from flask.json import dumps
from flask_sqlalchemy import SQLAlchemy
# from marshmallow import fields
# from marshmallow_sqlalchemy import ModelSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://v2:Jackson24@localhost/v2-python'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    todo_description = db.Column(db.String(100))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, todo_description):
        self.title = title
        self.todo_description = todo_description

    def __repr__(self):
        return f"{self.title} - {self.todo_descripton}"

db.create_all()

# class TodoSchema(ModelSchema):
#     class Meta(ModelSchema.Meta):
#         model = Todo
#         sqla_session = db.session
    
#     id = fields.Number(dumps_only=True)
#     title = fields.String(required=True)
#     todo_description = fields.String(required=True)


@app.route('/api/v1/todo', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = Todo(title=data['title'], todo_description=data['todo_description'])
    db.session.add(todo)
    db.session.commit()

    return jsonify({'id': todo.id})
