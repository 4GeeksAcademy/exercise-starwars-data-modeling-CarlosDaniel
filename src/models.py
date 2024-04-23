import os
from symtable import Class
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(120))
    since = Column(String(9))

class Favorites(Base):
    __tablename__ = 'favorites'
    User_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    Favorite_planet = Column(Integer,ForeignKey('planets.id'))
    Favorite_movie = Column(Integer,ForeignKey('movies.id'))
    Favorite_character = Column(Integer,ForeignKey('characters.id'))
    Favorite_vehicle = Column(Integer,ForeignKey('vehicles.id'))
        
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100),nullable=False)
    planet_population = Column(Integer)
    planet_area = Column(Integer)
    planet_gravity = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String)
    vehicle_model = Column(String)
    vehicle_type = Column(String)
    


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    Character_gender = Column(String)
    character_eye_color = Column(String)
    character_hair_color = Column(String)
    character_height = Column(Integer)
    character_planet = Column(Integer, ForeignKey('Planets.id'))
    character_vehicles = Column(Integer, ForeignKey('Vehicles.id'))

class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    movie_lenght_time = Column(Integer)
    movie_characters = Column(Integer, ForeignKey('Characters.id'))
    movie_vehicles = Column(Integer, ForeignKey('Vehicles.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
