import openai
import json

client = openai.OpenAI(
    api_key="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"
)

conversation = [
    {
        "role": "system",
        "content": """Your task is to check what python script should return, and then give explanation.
        Please give answer in format:
        answer: *what python script should return*
        explanation: *explanation*
        do not provide anything more
        """
    },
    {
        "role": "user",
        "content": "Please, tell me what should return the following scripts, as well as the explanation"
    }
]

while True:
    text = input()
    if text in ["quit", "exit"]:
        print("Do you want to save conversation to the file?")
        if input() in ["yes", "Y", "y"]:
            print("Provide name file: (without extension)")
            name_file = input()
            with open(f'{name_file}.json', 'w') as fp:
                json.dump(conversation, fp)
        break
    conversation.append({
        "role": "user",
        "content": text
    })

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #model="gpt-4",
        messages=conversation,
    )
    answer = stream.choices[0].message.content
    print(answer)
    conversation.append({
        "role": "assistant",
        "content": answer
    })