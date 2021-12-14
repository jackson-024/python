from flask import render_template, url_for, flash, redirect
from flask_login.utils import login_required
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import Users, Posts
from flask_blog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user


@app.route("/")
@login_required
def home():
    return render_template('home.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_pass)
        # user = Users.query.filter_by(username=form.username.data).first()
        db.session.add(user)
        db.session.commit()

        flash (f'Account created!!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash ('You are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash ('Login Unsuccessful!', 'danger')

    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))