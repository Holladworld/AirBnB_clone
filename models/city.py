#!/usr/bin/python3
'''Module container for class City'''

from models.base_model import BaseModel


class City(BaseModel):
    """Class for City instances"""
    state_id = ""
    name = ""
