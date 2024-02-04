#!/usr/bin/python3
"""
This module will define the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that represents a City
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
