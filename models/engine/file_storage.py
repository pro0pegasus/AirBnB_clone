#!/usr/bin/python3
"""
Module file_storage serialize and
deserialize JSON types
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Custom class for file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return dict repres of all objects
        """
        return self.__objects

    def new(self, object):
        """set in __objects  obj with  key
        <object class name>.id

        Args:
            object(obj): obj to write

        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        serializes __objects to JSON file
        (path: __file_path)
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, f)

    def reload(self):
        """
        deserialize JSON file to __objects, if JSON
        file exist, if not then nothing happens
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
