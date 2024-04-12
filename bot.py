import openai
import copy
import os
from dotenv import load_dotenv

class Bot(openai.OpenAI):
    def __init__(
            self, 
            system_info: str, 
            additional_info: str = None, 
            model: int = "gpt-3.5-turbo",
        ):
        load_dotenv(override=True)
        super(Bot, self).__init__()
        self.api_key = api_key = os.environ.get("OPENAI_API_KEY")
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
        

    def get(
            self, 
            request: str,
            previous_conversation: tuple[dict, dict] = None
            ):
        context = copy.deepcopy(self.context)
        if previous_conversation is not None:
            previous_question, previous_answer = previous_conversation
            context.append(previous_question)
            context.append(previous_answer)
        context.append({
            "role": "user",
            "content": request
        })
        stream = self.chat.completions.create(
            model=self.model,
            messages=context
        )
        answer = stream.choices[0].message.content

        return answer


