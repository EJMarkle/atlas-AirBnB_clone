#!/usr/bin/python3
"""
This module will define the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method to create an instance of User.
        """
        super().__init__(*args, **kwargs)
