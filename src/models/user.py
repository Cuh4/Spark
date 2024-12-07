"""
----------------------------------------------
Spark: An open-source recreation of YouTube.
https://github.com/Cuh4/Spark
----------------------------------------------

Copyright (C) 2024 Cuh4

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# // Imports
from __future__ import annotations

import peewee
from . import proxy

# // Main
class User(peewee.Model):
    """
    Represents a Spark user.
    """
    
    email = peewee.CharField(max_length = 320)
    username = peewee.CharField(max_length = 32, unique = True, index = True) # index != primary_key. all users will still have an ID
    display_name = peewee.CharField(max_length = 32)
    hashed_password = peewee.CharField(max_length = 64)
    is_admin = peewee.BooleanField(default = False)
    is_restricted = peewee.BooleanField(default = False)
    profile_url = peewee.CharField(max_length = 128, null = True)
    banner_url = peewee.CharField(max_length = 128, null = True)
    
    class Meta:
        database = proxy