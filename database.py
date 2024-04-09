from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import certifi



class DatabaseClient(MongoClient):
    def __init__(
            self,
            database_name = "Quiz",
            question_collection_name = "Questions"
        ):
        load_dotenv(override=True)
        super(DatabaseClient, self).__init__(
            os.environ.get("mongodb_uri"),
            server_api = ServerApi('1'),
            tlsCAFile = certifi.where()
            )
        self.database = self[database_name]
        self.question_collection = self.database[question_collection_name]
    
    def add_question(self, question):
        return self.question_collection.insert_one(question)

