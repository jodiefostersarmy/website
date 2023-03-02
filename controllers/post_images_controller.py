from models.PostImage import PostImage
from models.Post import Post
from schemas.PostImageSchema import book_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

post_images = Blueprint('post_images', __name__, url_prefix="/books/<int:book_id>/image")

@post_images.route("/", methods=["GET"])
@jwt_required()
def post_image_create(post_id):
    pass

@post_images.route("/<int:id>", methods=["GET"])
def book_image_show(book_id, id):
    pass

@post_images.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def book_image_delete(book_id, id):
    pass
