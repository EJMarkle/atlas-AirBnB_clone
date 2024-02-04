#!/usr/bin/python3
"""
This module will define the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that represents a Review.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
