#!/usr/bin/python3

"""
    Create class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Hbnb User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""

        super().__init__(*args, **kwargs)
