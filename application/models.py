from flask_login import UserMixin
from sqlalchemy.sql import func

from application import db

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(31), unique=True, nullable=False)
    password = db.Column(db.String(63), nullable=False)
    email = db.Column(db.String(127), unique=True, nullable=False)
    profile_pic = db.Column(db.String(255), default="default.jpg")
    is_active = db.Column(db.Boolean, default=True)
    join_date = db.Column(db.DateTime, default=func.now())

class Pokemon(db.Model, UserMixin):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    pokedex_number = db.Column(db.Integer, primary_key=True, nullable=False)
    catch_date = db.Column(db.DateTime, default=func.now())

class FavoritePokemon(db.Model, UserMixin):
    __tablename__ = "favorite_pokemons"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"))