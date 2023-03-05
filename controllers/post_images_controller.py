from models.PostImage import PostImage
from models.Post import Post
from schemas.PostImageSchema import post_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort, current_app, Response
from pathlib import Path
import boto3
from main import db

post_images = Blueprint('post_images', __name__, url_prefix="/posts/<int:post_id>/image")

@post_images.route("/", methods=["POST"])
@jwt_required()
def post_image_create(post_id):
    posts = Post.query.filter_by(id=post_id, user_id=get_jwt_identity())

    if posts.count() != 1:
        return abort(401, description="Invalid post")
    
    if "image" not in request.files:
        return abort(400, description="No image")
    
    image = request.files["image"]

    if Path(image.filename).suffix != ".png":
        return abort(400, description="Invalid file type")
    
    filename = f"{post_id}.png"
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    key = f"post_images/{filename}"
    bucket.upload_fileobj(image, key)

    if not(posts[0].post_image):
        new_image = PostImage()
        new_image.filename = filename
        posts[0].post_image = new_image
        db.session.commit()

    return ("", 200)

@post_images.route("/<int:id>", methods=["GET"])
def post_image_show(post_id, id):
    post_image = PostImage.query.filter_by(id=id, post_id=post_id).first()

    if not post_image:
        return abort(404, description="No post image")
    
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    filename = post_image.filename
    file_obj = bucket.Object(f"post_images/{filename}").get()

    return Response(
        file_obj['Body'].read(),
        mimetype='image/png',
        headers={"Content-Disposition": f"attachment;filename=image"}
    )

@post_images.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def post_image_delete(post_id, id):
    post = Post.query.filter_by(id=post_id, user_id=get_jwt_identity()).first()

    if not post:
        return abort(401, description="Invalid post")
    
    if post.post_image:
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        filename = post.post_image.filename

        bucket.Object(f"post_images/{filename}").delete()

        db.session.delete(post.post_image)
        db.session.commit()

    return jsonify("successfully removed")
