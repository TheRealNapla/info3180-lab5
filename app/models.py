# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text())
    poster = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def __repr__(self):
        return '<Movie %r>' % (self.title)