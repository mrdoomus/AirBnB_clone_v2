#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


class DB_Storage:
    """This is the class for DB_Storage
    Attributes:
        __name: Created engine
        __session: Session for queries
    """
    __engine = None
    __session = None

    def __init__(self):
        USER = os.environ.get('HBNB_MYSQL_USER')
        PASSWD = os.environ.get('HBNB_MYSQL_PWD')
        HOST = os.environ.get('HBNB_MYSQL_HOST')
        DB = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                USER, PASSWD, HOST, DB), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ All returns a dic with class instances
        """
        dic = {}
        if cls:
            for ins in self.__session.query(cls).all():
                dic[ins.__class__.__name__ + '.' + ins.id] = ins
        else:
            for ins in self.__session.query(
                    User, State, City, Amenity, Place, Review).all():
                dic[ins.__class__.__name__ + '.' + ins.id] = ins
        return dic

    def new(self, obj):
        """ New - adds a new object to the session
        """
        self.__session.add(obj)

    def save(self):
        """ Save - saves an object to the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete - deletes an object to the session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Delete - deletes an object to the session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
