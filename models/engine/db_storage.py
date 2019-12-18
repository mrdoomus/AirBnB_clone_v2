#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


class DB_Storage:
    __engine = None
    __session = None

    def __init__(self):
        USER = os.environ.get('HBNB_MYSQL_USER')
        PASSWD = os.environ.get('HBNB_MYSQL_PWD')
        HOST = os.environ.get('HBNB_MYSQL_HOST')
        DB = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(USER ,PASSWD, HOST, DB), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        self.__session = Session(self.__engine)
        """1 - No te pasan clase
        2 - Pasan clase"""
        if cls:
            key = "{}.{}".format(cls.__class__.__name__, cls.id)    


            """key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj"""
