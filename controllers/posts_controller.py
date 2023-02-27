from models.Post import Post
from main import db
from schemas.PostSchema import post_schema, posts_schema
from flask import Blueprint, request, jsonify
posts = Blueprint('posts', __name__, url_prefix="/posts")

@posts.route("/", methods=["GET"])
def post_index():
    # return all posts
    posts = Post.query.all()
    return jsonify(posts_schema.dump(posts))

@posts.route("/", methods=["POST"])
def post_create():
    #Create a new post
    post_fields = post_schema.load(request.json)

    new_post = Post()
    new_post.title = post_fields["title"]
    
    db.session.add(new_post)
    db.session.commit()
    
    return jsonify(post_schema.dump(new_post))

@posts.route("/<int:id>", methods=["GET"])
def post_show(id):
    #Return a single post
    post = Post.query.get(id)
    return jsonify(post_schema.dump(post))

@posts.route("/<int:id>", methods=["PUT", "PATCH"])
def post_update(id):
    #Update a post
    posts = Post.query.filter_by(id=id)
    post_fields = post_schema.load(request.json)
    posts.update(post_fields)
    db.session.commit()

    return jsonify(post_schema.dump(posts[0]))

@posts.route("/<int:id>", methods=["DELETE"])
def post_delete(id):
    #Delete a post
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return jsonify(post_schema.dump(post))
