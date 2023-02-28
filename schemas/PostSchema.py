from main import ma
from models.Post import Post
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
    
    title = ma.String(required=True, validate=Length(min=3))
    user = ma.Nested(UserSchema)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
