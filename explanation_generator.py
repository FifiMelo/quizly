from bot import Bot


class ExplanationGenerator(Bot):
    def __init__(self):
        super(ExplanationGenerator, self).__init__(
            system_info = """
Your task is to explain what python script does,
and then predict what is the value of variable "result".
Answer should be only value of the variable "result", do not provide anything else.
Please give answer in format:
explanation: *explanation*
answer: *what is the value of varaible "result" at the end*
do not provide anything more
""",
            additional_info = """
Please, explain me what the script does, 
and tell what is the value of varaible "result" at the end.
""",
            model = "gpt-3.5-turbo",
            continuous = False
        )
    
    def generate_explanation(
            self,
            question_code: str
    ):
        query = self.get(question_code)
        explanation_index = query.find("explanation: ")
        answer_index = query.find("answer: ")
        answer = query[answer_index + len("answer: "):]
        explanation = query[explanation_index + len("explanation: "):answer_index]
        return answer, explanation

