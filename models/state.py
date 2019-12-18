#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """ Adds every instance of City and returns a list """
            cities_dict = models.storage.all(City)
            cities_list = []
            for value in cities_dict.values():
                if value[id] == self.id:
                    cities_list.append(value)
            return cities_list
