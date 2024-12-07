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

# // Main
class BaseRouter(fastapi.APIRouter):
    """
    Represents a router for the API. Contains multiple API routes that can then be added to the API later under a group.
    """    
    
    def __init__(self, prefix: str, tags: list[str]):
        """
        Initializes a new instance of the BaseRouter class.

        Args:
            prefix (str): The prefix for the router
            tags (list[str]): The tags that best fit this router
        """        
        
        super().__init__(prefix = prefix, tags = tags)