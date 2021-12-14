from datetime import datetime
from flask_blog import db,  login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    post = db.relationship('Posts', backref='author', lazy=True)
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self 

    def __repr__(self):
        return f"{self.username} - {self.email}"

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(500)) 
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self 

    def __repr__ (self):
        return f"{self.title} - {self.content} - {self.date_posted}"
