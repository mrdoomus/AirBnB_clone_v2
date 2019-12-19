#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base
import os


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_STORAGE') == 'db':
        place_amenities = relationship(
            "Place", secondary=place_amenity, backref="amenities")
