#!/usr/bin/python3
"""
This module will define the BaseModel class.
"""
import uuid
import datetime


class BaseModel:
    """
    Class that defines all common members for other classes.
    """

    def __init__(self) -> None:
        """Creates an instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self) -> None:
        """Updates the field updated_at with current datetime."""
        self.updated_at = datetime.datetime.now()