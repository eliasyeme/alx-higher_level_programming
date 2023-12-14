#!/usr/bin/python3
"""
contains the class definition of a City
"""
from model_city import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    defines a City

    Attributes:
        id (int): id of the city
        name (str): name of the city
        state_id (int): id of the state
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
