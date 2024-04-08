from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os

load_dotenv()

class DB:
    """
    A class representing a MongoDB database connection.

    Attributes:
        uri (str): The connection URI for the MongoDB database.
        client (pymongo.MongoClient): The MongoDB client object.

    Methods:
        __init__(): Initializes a new instance of the DB.
    """

    uri =f"mongodb+srv://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('CLUSTER')}.1zyzpgd.mongodb.net/?retryWrites=true&w=majority&appName={os.getenv('CLUSTER')}"

    def __init__(self):
        """
        Initializes a new instance of the DB class.

        Parameters:
            None

        Returns:
            None
        """
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        


