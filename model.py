"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """This is our cupcake"""
    
    __tablename__ = "cupcakes"
    
    id = db.column(db.Integer , primary_key = True, autoincrement=True)
    flavor = db.column(db.Text , nullable = False)
    size = db.column(db.text , nullable = False)
    rating = db.column(db.float , nullable = False)
    image = db.column(db.text , nullable = False , default = DEFAULT_IMAGE)
    