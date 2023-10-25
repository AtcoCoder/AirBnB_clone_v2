#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of
            City instances with state_id that equal to the current
            State.id"""
            from models import storage
            from models.city import City
            all_cities = storage.all(City).values()
            cities = []
            for city in all_cities:
                if city.state_id == self.id:
                    cities.append(city)
            return cities
