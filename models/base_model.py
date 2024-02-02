#!/usr/bin/python3
"""
This module will define the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class that defines all common members for other classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Constructor method to create an instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    ))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self) -> str:
        """Gives a user friendly string representation of BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self) -> None:
        """Updates the field updated_at with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Returns a dictionary rep of the instance."""
        r_dict = self.__dict__.copy()
        # Get only the instance fields.
        r_dict['__class__'] = self.__class__.__name__
        # Add the __class__ key with the class name of the object.
        r_dict['created_at'] = self.created_at.isoformat()
        r_dict['updated_at'] = self.updated_at.isoformat()
        # Convert instance fields to ISO format string.
        return r_dict
