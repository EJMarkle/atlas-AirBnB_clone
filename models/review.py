#!/usr/bin/python3
"""
This module will define the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that represents a Review.
    """
    place_id = ""
    user_id = ""
    text = ""
