from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import ASCENDING
import certifi



class DatabaseClient(MongoClient):
    def __init__(
            self,
            key: str,
            database_name = "Quiz",
            question_collection_name = "Questions",
            tags_collection_name = "Tags"
        ):
        super(DatabaseClient, self).__init__(
            key,
            server_api = ServerApi('1'),
            tlsCAFile = certifi.where()
            )
        self.database = self[database_name]
        self.question_collection = self.database[question_collection_name]
        self.tags_collection = self.database[tags_collection_name]
    
    def add_question(self, question):
        """
        This function adds quesiton to the database as well as updates 
        "Tags" collection.
        """
        for tag in question["tags"]:
            result = self.tags_collection.update_one({"tag": tag}, {"$inc":{"count": 1}})
            if result.modified_count == 0:
                self.tags_collection.insert_one(
                    {
                        "tag": tag,
                        "count": 1
                    }
                )

        return self.question_collection.insert_one(question)
    
    def get_tag(self):
        return self.tags_collection.find().sort("count", ASCENDING).limit(1).next()["tag"]
        

    


