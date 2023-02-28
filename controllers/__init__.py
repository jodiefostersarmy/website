from controllers.index_controller import index
from controllers.posts_controller import posts
from controllers.auth_controller import auth

registerable_controllers = [
    auth,
    index,
    posts
]
