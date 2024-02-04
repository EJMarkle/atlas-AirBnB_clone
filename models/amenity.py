#!/usr/bin/python3
"""
This module will define the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class that represents an Amenity
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
