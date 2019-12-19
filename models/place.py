#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, Table, ForeignKey, Integer, Float
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from models.base_model import Base
import os
import models


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.environ.get('HBNB_STORAGE') == 'db':
        metadata = Base.metadata
        place_amenity = Table('place_amenity', metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'), primary_key=True,
                                     nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True,
                                     nullable=False))
        reviews = relationship("Review", cascade="delete", backref="places")
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """ """
            dict_revs = models.storage.all(Review)
            list_revs = []
            for value in dict_revs.values():
                if value[id] == self.id:
                    list_revs.append(value)
            return list_revs

        @property
        def amenities(self):
            """ """
            dict_amenities = models.storage.all(Amenity)
            list_amenities = []
            for value in dict_amenities.values():
                if Amenity.id in self.amenity_ids:
                    list_amenities.append(value)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """ """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
