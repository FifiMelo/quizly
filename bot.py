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


