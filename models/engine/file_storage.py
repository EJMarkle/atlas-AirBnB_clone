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
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                obj_class = getattr(sys.modules[self.__module__], class_name)
                obj = obj_class(**obj_dict)
                self.__objects[key] = obj
