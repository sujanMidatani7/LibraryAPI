from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os

load_dotenv()

class DB:
    uri =f"mongodb+srv://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@{os.getenv("CLUSTER")}.1zyzpgd.mongodb.net/?retryWrites=true&w=majority&appName={os.getenv("CLUSTER")}"
    def __init__(self):
        
        self.client=MongoClient(self.uri, server_api=ServerApi('1'))
        


