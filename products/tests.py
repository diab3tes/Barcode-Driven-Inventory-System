from mongoengine import connect
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

connect(
    db=MONGO_DB_NAME,
    host=MONGO_URI,
    tls=True,
    serverSelectionTimeoutMS=30000,  # 30-second timeout
)


