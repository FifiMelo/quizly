from bot import Bot


class QuestionGenerator(Bot):
    def __init__(self, tag: str):
        super(QuestionGenerator, self).__init__(
            system_info = """
            Your task is to create python puzzle chunk. 
            The chunk should end in statement result = ..., variable that will store the result of the code.
            Please, don't provide anything else than the code, no questions, no answers, no hints, nothing.
            """,
            additional_info = None,
            model = "gpt-3.5-turbo",
            continuous = True,
        )
        self.tag = tag
        self.number_of_generated_questions = 0
        

    
    def generate(
            self,
            difficulty_change: int = 0
        ):
        if self.number_of_generated_questions == 0:
            request = f"""
                Give me one python puzzle involving {self.tag}. It should have at most 5 lines of code.
                Store the value to be estimated in variable "result".
                """
        else:
            if difficulty_change > 0:
                request = """
                    Very nice, but this time please give me something slightly more challenging.
                    """
            if difficulty_change < 0:
                request = """
                    Very nice, but this one was too hard. Please give me something a little bit easier.
                    """
            if difficulty_change == 0:
                request = """
                    Very nice, please give me next one, on same difficulty level.
                    """
        self.number_of_generated_questions += 1
        return self.get(
            request = request
        )




    
