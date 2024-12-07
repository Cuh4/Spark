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
from log import logger

from .base import BaseRouter
from .user import router as UserRouter

# // Main
def add_routers(app: fastapi.FastAPI):
    """
    Adds all routers to the app.

    Args:
        app (fastapi.FastAPI): The app to use.
    """
    
    for router in [router for router in locals().values() if isinstance(router, fastapi.APIRouter) and router != BaseRouter]:
        logger.info(f"Adding router: {router.prefix}")
        app.include_router(router())