from bot import Bot


class ExplanationGenerator(Bot):
    def __init__(self):
        super(ExplanationGenerator, self).__init__(
            system_info = """
            Your task is to check what python script does,
            and tell what is the value of variable "result", and then give explanation.
            Please give answer in format:
            answer: *what python script should return*
            explanation: *explanation*
            do not provide anything more
            """,
            additional_info = """
            Please, tell me what should return the following scripts, 
            as well as the explanation
            """,
            model = "gpt-3.5-turbo",
            continuous = True
        )
    
    def generate_explanation(
            self,
            question_code: str
    ):
        answer = self.get(question_code)
        return answer

