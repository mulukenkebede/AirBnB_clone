#!/usr/bin/python3
"""class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """inheritated User from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    
