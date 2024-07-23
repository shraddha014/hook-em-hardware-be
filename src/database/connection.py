from dotenv import load_dotenv, find_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv(find_dotenv())

# fetchong username and password from env file
password = os.environ.get('MONGODB_PASSWORD')
username = os.environ.get('MONGODB_USERNAME')

connectionString = f"mongodb+srv://{username}:{password}@harware-cluster.vgcxnga.mongodb.net/?retryWrites=true&w=majority&appName=harware-cluster"

# Create a new client and connect to the server
client = MongoClient(connectionString, server_api=ServerApi('1'))
