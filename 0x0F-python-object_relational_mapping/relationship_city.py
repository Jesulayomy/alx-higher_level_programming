#!/usr/bin/python3

"""
    This module contains the city class and Base
"""

from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ The City class, child of Base married to State? """

    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True)

    name = Column(
            String(128),
            nullable=False)

    state_id = Column(
            Integer,
            ForeignKey("states.id"),
            nullable=False)
