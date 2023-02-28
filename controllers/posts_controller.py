from models.Post import Post
from models.User import User
from main import db
from schemas.PostSchema import post_schema, posts_schema
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import joinedload

posts = Blueprint('posts', __name__, url_prefix="/posts")

@posts.route("/", methods=["GET"])
def post_index():
    # return all posts
    posts = Post.query.options(joinedload("user")).all()
    return jsonify(posts_schema.dump(posts))

@posts.route("/", methods=["POST"])
@jwt_required()
def post_create():
    #Create a new post
    post_fields = post_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid User")

    new_post = Post()
    new_post.title = post_fields["title"]
    
    user.posts.append(new_post)

    db.session.commit()
    
    return jsonify(post_schema.dump(new_post))

@posts.route("/<int:id>", methods=["GET"])
def post_show(id):
    #Return a single post
    post = Post.query.get(id)
    return jsonify(post_schema.dump(post))

@posts.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def post_update(id):
    #Update a post
    post_fields = post_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    posts = Post.query.filter_by(id=id, user=user.id)

    if posts.count() != 1:
        return abort(401, description="Unauthorised to update this book")

    posts.update(post_fields)
    db.session.commit()

    return jsonify(post_schema.dump(posts[0]))

@posts.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def post_delete(id):
    #Delete a post
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    post = Post.query.filter_by(id=id, user_id=user.id).first()

    if not post:
        return abort(400)
    
    db.session.delete(post)
    db.session.commit()

    return jsonify(post_schema.dump(post))
