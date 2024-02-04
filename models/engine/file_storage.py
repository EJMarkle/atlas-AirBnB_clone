#!/usr/bin/python3
"""
This module will define the FileStorage class.
"""
import json
import os
import sys


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

        class_list = [BaseModel]
        
        if not os.path.isfile(FileStorage.__file_path):
            return
        map = {cls.__name__: cls for cls in class_list}

        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
            FileStorage.__objects = {}
            for key in data:
                name = key.split('.')[0]
                FileStorage.__objects[key] = map[name](**data[key])
