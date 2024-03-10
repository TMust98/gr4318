from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        uname = form.username.data
        pw = form.password.data
        flash(f'Логин {uname}, {pw}', "info")
        flash(f'Логин {uname}, {pw}', "danger")
        flash(f'Логин {uname}, {pw}', "warning")
        flash(f'Логин {uname}, {pw}', "success")
        return redirect(url_for('login'))

    return render_template('login.html', form=form, title="Вход")