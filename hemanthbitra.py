import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# List all environment variables
for key, value in os.environ.items():
    print(f"{key}={value}")
