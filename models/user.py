#!/usr/bin/python3

"""User"""

from models.base_model import BaseModel

class User(BaseModel):
    """initialization of class"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
