from flask import Flask
from flask import redirect
from flask import request
from flask import json
from flask import render_template
from flask_menu import Menu, register_menu
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

from flask_wtf.csrf import CsrfProtect,generate_csrf

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Length

app = Flask(__name__,static_url_path='',static_folder='static')


CsrfProtect(app)
app.config.update(
    DEBUG=True,
    WTF_CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/content')
def content_page():
    return render_template('content.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)











