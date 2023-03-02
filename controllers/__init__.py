from controllers.index_controller import index
from controllers.posts_controller import posts
from controllers.auth_controller import auth
from controllers.post_images_controller import post_images

registerable_controllers = [
    auth,
    index,
    posts,
    post_images
]
