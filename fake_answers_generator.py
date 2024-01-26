from bot import Bot


class FakeAnswersGenerator(Bot):
    def __init__(self):
        super(FakeAnswersGenerator, self).__init__(
            system_info = """
Your task is to create answers to a python script puzzle,
one, that is a true answers, and three, that are wrong, but looks like correct.
You will be given python script.
Please give the answer in format:
correct_answer: *what python script really returns*
fake_answer1: *first fake answer*
fake_answer2: *second fake answer*
fake_answer3: *third fake answer*     
""",
            additional_info = """
Please, tell me what should return the following scripts, as well as the fake answers.
""",
            model = "gpt-3.5-turbo",
            continuous = False
        )
    
    
    def generate_fake_answers(
            self,
            question_code: str
    ):
        query = self.get(question_code)

        real_answer_index = query.find("correct_answer: ")
        fake_answer1_index = query.find("fake_answer1: ")
        fake_answer2_index = query.find("fake_answer2: ")
        fake_answer3_index = query.find("fake_answer3: ")

        real_answer = query[real_answer_index:fake_answer1_index]
        fake_answer1 = query[fake_answer1_index:fake_answer2_index]
        fake_answer2 = query[fake_answer2_index:fake_answer3_index]
        fake_answer3 = query[fake_answer3_index:]

        return real_answer, [fake_answer1, fake_answer2, fake_answer3]
        



