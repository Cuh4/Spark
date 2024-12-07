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
import fastapi

from . import BaseRouter

# // Main
class UserRouter(BaseRouter):
    """
    A router containing routes for user-related operations.
    """    
    
    def __init__(self):
        """
        Initializes a new instance of the UserRouter class.
        """
        
        super().__init__(prefix = "/user", description = "Contains routes for user-related operations, like signing up, searching for users, etc.", tags = ["User", "Auth"])