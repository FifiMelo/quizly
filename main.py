from batch_creator import generate_batch
from database import DatabaseClient



def main():
    dbClient = DatabaseClient()
    while True:
        tag = dbClient.get_tag()
        for puzzle in generate_batch(tag):
                dbClient.add_question(puzzle)
        












if __name__ == '__main__':
    main()




