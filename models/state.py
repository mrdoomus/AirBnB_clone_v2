#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models.engine.file_storage
from models.city import City
from models import storage


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        """  """
        cities_dict = storage.all(City)
        cities_list = []
        for value in cities_dict.values():
            if value[id] == self.id:
                cities_list.append(value)
        return cities_list
