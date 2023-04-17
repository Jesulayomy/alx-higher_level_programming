#!/usr/bin/python3

"""
    This module contains the state class and Base
"""

from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, MetaData

md = MetaData()
Base = declarative_base(metadata=md)


class State(Base):
    """ The state class, child of Base """

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True)

    name = Column(
            String(128),
            nullable=False)

    cities = relationship("City", backref='states')
