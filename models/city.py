#!/usr/bin/python3
"""
This module will define the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that represents a City
    """
    state_id = ""
    name = ""
