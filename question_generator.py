from bot import Bot


class QuestionGenerator(Bot):
    def __init__(self, tag: str):
        super(QuestionGenerator, self).__init__(
            system_info = """
Your task is to create python puzzle chunk. 
The chunk should end in statement result = ..., variable that will store the result of the code.
Please, don't provide anything else than the code, no questions, no answers, no hints, nothing.
Please, don't use random numbers, the puzzle must be deterministically answerable.
Please, make the puzzle computationally simple, good for humans.
""",
            additional_info = None,
            model = "gpt-3.5-turbo"
        )
        self.tag = tag
        self.number_of_generated_questions = 0
        
    def generate_question(self,
        previous_question: str = None,
        difficulty_change: int = 0
        ):
        if previous_question is None:
            request = f"""
Give me one python puzzle involving {self.tag}. It should have at most 5 lines of code.
Store the value to be estimated in variable "result".
"""
            return self.get(
                request = request
            )
        previous_conversation = (
                    {
                        "role": "user",
                        "content": f"""
                        Give me one python puzzle involving {self.tag}. It should have at most 5 lines of code.
Store the value to be estimated in variable "result".
"""
                    },
                    {
                        "role": "assistant",
                        "content": previous_question
                    }
                )
        
        if difficulty_change == 0:
                request = """
Very nice, please give me next one, on the same difficulty level.
"""
        if difficulty_change > 0:
                request = """
Very nice, but this time please give me something slightly more challenging.
"""
        if difficulty_change < 0:
                request = """
Very nice, but this one was too hard. Please give me something a little bit easier.
"""

        return self.get(
             request = request,
             previous_conversation = previous_conversation
        )
            





    
