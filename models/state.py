#!/usr/bin/python3
"""
This module will define the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that represents a State
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
