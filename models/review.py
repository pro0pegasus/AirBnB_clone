#!/usr/bin/python3
"""
Define Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent review

    Attributes:
        place_id (str): Place id
        user_id (str): Usr id
        text (str): text of review

    """
    place_id = ""
    user_id = ""
    text = ""
