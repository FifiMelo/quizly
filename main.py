from batch_creator import generate_batch
from database import DatabaseClient
import openai
import json


def main():
    with open("./env.json") as file:
        data = json.load(file)
    openai.api_key = data["OPENAI_API_KEY"]
    dbClient = DatabaseClient()
    while True:
        tag = dbClient.get_tag()
        for puzzle in generate_batch(tag):
                dbClient.add_question(puzzle)
        












if __name__ == '__main__':
    main()




