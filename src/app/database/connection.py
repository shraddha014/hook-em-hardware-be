# app/database/connection.py
from dotenv import load_dotenv, find_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.errors import ConfigurationError
import certifi

def db_connection():
    try:
        load_dotenv(find_dotenv())

        # Fetching username and password from env file
        password = os.environ.get('MONGODB_PASSWORD')
        username = os.environ.get('MONGODB_USERNAME')

        connectionString = f"mongodb+srv://{username}:{password}@hardware-cluster.vgcxnga.mongodb.net/?retryWrites=true&w=majority&appName=hardware-cluster"

        # Create a new client and connect to the server
        client = MongoClient(connectionString, tlsCAFile=certifi.where())
        hookem_db = client["hook-em-database"]
        return hookem_db
    except ConfigurationError as e:
        print(f"Something went wrong: {e}")
        return None
