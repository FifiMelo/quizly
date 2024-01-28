from icecream import ic

def get_real_answer(code: str):

    result_dict = dict()

    try:
        exec(code, result_dict)

    except Exception as e:
        return False, None
    
    if not "result" in result_dict:
        return False, None
    
    return  result_dict["result"], True
    
def answers_correct(real_answer, answers):
    """
    Answers from chatgpt will always come as strings, but they can represent all possible
    types, numbers, arrays, dictionaries ect.
    Purpose of this function is to compare these answers, 
    and return True only if all of them are correct.
    """
    answer_dict = dict()
    for index in range(len(answers)):

        answer = transform_answer(answers[index])
        # strings need to be treated separately (purpose of try catching)

        try:
            exec(f"""var = {answer}""", answer_dict)
        except Exception as e:
            ic(e)
            exec(f"""var = "{answer}" """, answer_dict)

        if not answer_dict["var"] == real_answer:
            return False
    return True



def transform_answer(answer: str):
    phrases = [
        'The value of the "result" variable at the end is',
        'The value of the variable "result" at the end is',
        'The value of variable "result" at the end is'
    ]
    for phrase in phrases:
        if answer[:len(phrase)] == phrase:
            return answer[len(phrase):-1]
    return answer

if __name__ == '__main__':
    print(transform_answer('The value of the "result" variable at the end is 11.'))
