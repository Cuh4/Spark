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
from passlib.context import CryptContext

# // Main
password_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str:
    """
    Hashes a password for security.

    Args:
        password (str): The raw password.

    Returns:
        str: The hashed password
    """
    
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password.

    Args:
        plain_password (str): The raw password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    
    return password_context.verify(plain_password, hashed_password)