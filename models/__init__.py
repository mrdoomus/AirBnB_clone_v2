#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

HBNB_STORAGE = os.environ.get('HBNB_TYPE_STORAGE')

if HBNB_STORAGE == 'db':
    from models.engine.db_storage import DB_Storage
    storage = DB_Storage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
