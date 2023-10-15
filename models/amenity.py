#!/usr/bin/python3
"""
Mod for Amenty class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenty class

    Attributes:
        name(str): amenty name

    """
    name = ""
