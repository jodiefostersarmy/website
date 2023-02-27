from main import db
from flask import Blueprint, jsonify

index = Blueprint('index', __name__)

@index.route("/")
def home_page():
    return "This will be my landing page for my website/portfolio site"

@index.route('/contact')
def contact_page():
    return "contact page"
