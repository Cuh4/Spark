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
import peewee
from log import logger

# // Main
proxy = peewee.DatabaseProxy()
from .user import User

def add_models(database: peewee.Database):
    """
    Adds all models to the database.

    Args:
        database (peewee.Database): The database to mount the models to.
    """    
    
    proxy.initialize(database)
    
    logger.info("Adding models to database (tables).")
    database.create_tables([model for model in locals().values() if isinstance(model, peewee.ModelBase)])