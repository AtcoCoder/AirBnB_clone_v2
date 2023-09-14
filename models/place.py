#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True))
storage_type = getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    id = Column(String(60), primary_key=True)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    cities = relationship('City', back_populates='places')
    user = relationship('User', back_populates='places')
    amenity_ids = []
    if storage_type == 'db':
        reviews = relationship('Review',
                               back_populates='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity',
                             secondary='place_amenity',
                             viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with
            place_id == Place.id"""
            from models.review import Review
            from models import storage
            review_list = []
            for review_key, review in storage.all(Review):
                placd_id = review.place_id
                if place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter attr that returns the list of
            Amenity instances based on the attribute amenity_ids
            that contains all Amenity.id linked to the Place"""
            from models.amenity import Amenity
            from models import storage
            amenity_list = []
            for amenity_key, amenity in storage.all(Amenity).items():
                amenity_id = amenity_key.split('.')[1]
                if amenity_id in amenity_ids and amenity not in amenity_list:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, instance):
            """Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids.
            """
            from models.amenity import Amenity
            if isinstance(instance, Amenity):
                self.amenity_ids = instance.id

        def append(self, instance):
            """Appends to the amenities ids list"""
            self.amenity_ids = self.amenity_ids + [instance.id]
            return self.amenity_ids
