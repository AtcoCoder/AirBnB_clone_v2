#!/usr/bin/python3
"""Database engine module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


USER = getenv('HBNB_MYSQL_USER')
PASSWORD = getenv('HBNB_MYSQL_PWD')
HOST = getenv('HBNB_MYSQL_HOST')
DATABASE = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor of the class"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            USER, PASSWORD, HOST, DATABASE), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base = declarative_base()
            Base.metadata.drop_all(self)

    def all(self, cls=None):
        """"Query on the current database session all objects depending
        of the class name 'cls', if cls is none is then all classes"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.base_model import BaseModel
        cls_dict = {}
        cls_list = []
        if cls is None:
            cls_list += [State, City, User, Place, Review]
        else:
            cls_list.append(cls)
        for a_cls in cls_list:
            objs = self.__session.query(a_cls).all()
            for obj in objs:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                cls_dict[key] = obj
        return cls_dict

    def new(self, obj):
        """Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database if not exists """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.base_model import BaseModel, Base

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Method to remove session from registry"""
        self.__session.remove()
