#!/usr/bin/python3
"""
This module will define the FileStorage class.
"""
import json


class FileStorage:
    """Class to serialize and deserialized instances to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary __objects."""
        return  self.__objects
    
    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        