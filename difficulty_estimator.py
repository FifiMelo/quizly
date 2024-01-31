from bot import Bot
from icecream import ic

class DifficultyEstimator(Bot):
    def __init__(self):
        super(DifficultyEstimator, self).__init__(
            system_info = """
Your task is estimate difficulty of a python script puzzle,
at the scale of 1-100, as well as provide correct answer to the puzzle.
You will be given python script.
Please give the answer in format:
answer: *what python script should return*
difficulty: *difficulty on the scale of 1-100*
Please do not provide anything else.
""",
            additional_info ="""
Please, tell me what should return the following scripts, as well as the difficulty.
""",
            model = "gpt-3.5-turbo"
        )
    def estimate_difficulty(
            self, 
            question: str
            ):
        
        
        query = self.get(question)
        answer_index = query.find("answer: ")
        difficulty_index = query.find("difficulty: ")

        answer = query[answer_index + len("answer: "):difficulty_index]
        difficulty = query[difficulty_index + len("difficulty: "):]

        return answer, difficulty