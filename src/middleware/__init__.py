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
from starlette.middleware.base import BaseHTTPMiddleware

from log import logger
from .telemetry import TelemetryMiddleware

# // Main
all = [middleware for middleware in locals().values() if isinstance(middleware, type) and issubclass(middleware, BaseHTTPMiddleware) and middleware != BaseHTTPMiddleware]

def add_middleware(app: fastapi.FastAPI):
    """
    Adds all middleware to the app.

    Args:
        app (fastapi.FastAPI): The app to use.
    """

    for middleware in all:
        logger.info(f"Adding middleware: {middleware.__name__}")
        app.add_middleware(middleware)