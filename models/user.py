#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.review import Review
from sqlalchemy.orm import relationship
from models.base_model import Base


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="delete", backref="user")
    reviews = relationship("Review", cascade="delete", backref="user")
