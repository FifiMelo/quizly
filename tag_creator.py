from bot import Bot
from icecream import ic

class TagCreator(Bot):
    def __init__(self):
        super(TagCreator, self).__init__(
            system_info = """
Your task is to provide tags for a python script.
You will be given python script.
There should be 3 - 6 tags.
Please give the answer in format:
tags: *tags separated with comas*
Do not provide anyting else than tags.
""",
            additional_info = "Please, give me the tags about this script",
            model = "gpt-3.5-turbo"
        )
    
    def create_tags(self, question):
        query = self.get(
            request = question
        )
        query = query.replace('tags:', '')
        tags = query.split(',')

        return [tag.strip() for tag in tags]
    