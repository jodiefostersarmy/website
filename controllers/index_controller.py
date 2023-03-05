from main import db
from flask import Blueprint, jsonify

index = Blueprint('index', __name__)

@index.route("/")
def home_page():
    return "I love you Kit Anne"

@index.route('/contact')
def contact_page():
    return "contact page"
