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
import toml

# // Main
with open("../config.toml", "r") as file:
    config = toml.load(file)

mode: str = config["environment"]["mode"]

if mode == "dev":
    host: str = config["dev"]["host"]
    port: int = config["dev"]["port"]
    log_level: int = config["dev"]["log_level"]
else:
    host: str = config["prod"]["host"]
    port: int = config["prod"]["port"]
    log_level: int = config["prod"]["log_level"]
    
log_file: str = config["logging"]["file"]

database_host: str = config["database"]["host"]
database_port: int = config["database"]["port"]
database_name: str = config["database"]["name"]
database_user: str = config["database"]["user"]
database_password: str = config["database"]["password"]

with open("../VERSION") as file:
    version: str = file.read()