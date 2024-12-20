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

import uvicorn
from fastapi import FastAPI

from middleware import add_middleware
from routes import add_routers
from models import add_models

from log import logger
import config

# // Main
database = peewee.PostgresqlDatabase(
    database = config.database_name,
    host = config.database_host,
    port = config.database_port,
    user = config.database_user,
    password = config.database_password
)

app = FastAPI(
    title = "Spark",
    description = "An API for the open-source recreation of YouTube, Spark.",
    version = config.version,
    debug = config.mode == "dev",

    license_info = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0"
    }
)

app.add_exception_handler(peewee.InternalError, lambda request, exc: logger.critical(f"Internal error: {exc}"))
add_middleware(app)
add_routers(app)
add_models(database)

app.add_event_handler("startup", lambda: logger.info("Spark API has started."))
app.add_event_handler("shutdown", lambda: logger.info("Spark API has stopped."))

if __name__ == "__main__":
    uvicorn.run(app, host = config.host, port = config.port, log_level = config.log_level)