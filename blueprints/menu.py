from flask import Blueprint, render_template

menu = Blueprint('order', __name__)

@menu.route('/')
def index():
    return render_template('index.html')