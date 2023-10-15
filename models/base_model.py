#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base for all classes in AirBnb console proj

    Arttributes:
        id(str): handle unique user id
        created_at: assign curr datetime
        updated_at: update curr datetime

    Methods:
        __str__: print class name, id, and creates dict
        reps of input vals
        save(self): update inst arttrib with curr datetime
        to_dict(self): return dict vals of inst obj

    """

    def __init__(self, *args, **kwargs):
        """Public inst attrib init
        after creation

        Args:
            *args(args): arguments
            **kwargs(dict): attrib vals

        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Return string repr of class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update public inst attrib:
        'updated_at' - with curr datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method return dict containing all 
        keys/values of __dict__ inst
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
