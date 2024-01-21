



class Puzzle:
    def __init__(
            self,
            content: str,
            tags: list[str],
            difficulty: int,
            answer: str,
            fake_answers: list[str],
            explanation: str
        ):
        self.content = content
        self.tags = tags
        self.difficulty = difficulty
        self.answer = answer
        self.fake_answers = fake_answers
        self.explanation = explanation

    def get_content(self):
        return self.content
    
    def get_tags(self):
        return self.tags
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_answer(self):
        return self.answer
    
    def get_fake_answers(self):
        return self.fake_answers
    
    def get_explanation(self):
        return self.explanation

