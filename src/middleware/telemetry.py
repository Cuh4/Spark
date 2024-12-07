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
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from log import logger

# // Main
class TelemetryMiddleware(BaseHTTPMiddleware):
    """
    Logs all HTTP requests to the API, etc.
    """
    
    def __init__(self, app: fastapi.FastAPI):
        """
        Initializes the middleware instance.

        Args:
            app (fastapi.FastAPI): The FastAPI app
        """        
        
        super().__init__(app)
        
    async def dispatch(self, request: fastapi.Request, call_next: RequestResponseEndpoint) -> fastapi.Response:
        """
        Called when a request is received

        Args:
            request (fastapi.Request): The request
            call_next (RequestResponseEndpoint): The endpoint callback

        Returns:
            fastapi.Response: The response for the request
        """
        
        logger.info(f"[{request.client.host}:{request.client.port}] Received request: {request.method} -> {request.url}")
        logger.info(f"Params: {request.query_params}")
        
        response  = await call_next(request)
        return response