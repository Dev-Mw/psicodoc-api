from django.db import models
from dataclasses import dataclass


@dataclass
class UsersModel:
    first_name: str
    last_name: str
    username: str
    email: str
    is_active: str
