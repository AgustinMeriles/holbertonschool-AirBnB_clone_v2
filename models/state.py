#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        """Returns the list of cities associated with this state"""
        from models import storage
        cities = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
