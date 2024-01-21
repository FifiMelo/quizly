import openai
import copy

class Bot(openai.OpenAI):
    def __init__(
            self, 
            system_info: str, 
            additional_info: str = None, 
            model: int = "gpt-3.5-turbo",
            continuous: bool = False
        ):
        super(Bot, self).__init__(api_key = "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")
        self.continuous = continuous
        self.model = model
        self.context = [
            {
                "role": "system",
                "content": system_info
            }
        ]
        if not additional_info is None:
            self.context.append({
                "role": "user",
                "content": additional_info
            })
        

    def get(self, request: str):
        if self.continuous:
            self.context.append({
                "role": "user",
                "content": request
            })
            stream = self.chat.completions.create(
                model=self.model,
                messages=self.context
            )
            answer = stream.choices[0].message.content
        else:
            context = copy.deepcopy(self.context)
            context.append({
                "role": "user",
                "content": request
            })
            stream = self.chat.completions.create(
                model=self.model,
                messages=self.context
            )
            answer = stream.choices[0].message.content

        return answer


if __name__ == '__main__':
    Question_generator = Bot(
        system_info=""""Your task is to create python puzzle chunk. 
        The chunk should end in statement result = ..., variable that will store the result of the code.
        Please, don't provide anything else than the code, no questions, no answers, no hints, nothing.
        """,
        continuous=True
    )
    print(Question_generator.get(
        """
        Give me one python puzzle involving python. It should have at most 5 lines of code.
        Difficulty should be around 25, on a sclty should be around 25, on a scale 1-100.
        Store the value to be estlty should be around 25, on a scale 1-100.
        Store the value to be estimated in variable "result"."""
        ))
    print(Question_generator.get("A bit harder one, please"))