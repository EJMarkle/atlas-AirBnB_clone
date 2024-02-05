#!/usr/bin/python3
"""
This module will define the FileStorage class.
"""
import json
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class to serialize and deserialized instances to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file."""
        seri_objects = {}
        for key, obj in self.__objects.items():
            seri_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(seri_objects, file)

    def reload(self):
        """"Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User

        class_list = [BaseModel, User, State, City, Amenity, Place, Review]

        if not os.path.isfile(FileStorage.__file_path):
            return
        map = {cls.__name__: cls for cls in class_list}

        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
            FileStorage.__objects = {}
            for key in data:
                name = key.split('.')[0]
                FileStorage.__objects[key] = map[name](**data[key])
