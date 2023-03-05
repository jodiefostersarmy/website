from main import db
from models.PostImage import PostImage

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_image = db.relationship("PostImage", backref="post", uselist=False)

    def __repr__(self):
        return f"<Post {self.title}>"
