#!/usr/bin/python3
"""
Define User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent  User

    Attributes:
        email (str): usr email
        password (str): usr PW
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
