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



    
def check_answers(real_answer, answers, correct_answers = True):
    """
    Answers from chatgpt will always come as strings, but they can represent all possible
    types, numbers, arrays, dictionaries ect.
    Purpose of this function is to compare these answers, 
    and return True only if all of them are correct.
    (or return True only if all of them are wrong when correct_answers = False)
    """
    answer_dict = dict()
    for index in range(len(answers)):

        answer = transform_answer(answers[index])
        # strings need to be treated separately (purpose of try catching)
        try:
            try:
                exec(f"""var = {answer}""", answer_dict)
            except Exception as e:
                print(e, answer)
                exec(f"""var = "{answer}" """, answer_dict)
        except Exception as e:
            ic(e, real_answer, answers)
            return False

        if (answer_dict["var"] == real_answer) != correct_answers:
            return False
    return True



def transform_answer(answer: str):
    phrases = [
        'The value of the "result" variable at the end is',
        'The value of the variable "result" at the end is',
        'The value of variable "result" at the end is',
        'The value of the variable "result" at the end will be',
        'The value of the variable "result" will be',
        'The value of the variable "result" at the end is',
        "The value of the variable 'result' at the end is"
    ]
    for phrase in phrases:
        if answer[:len(phrase)] == phrase:
            return answer[len(phrase):-1]
    answer = answer.replace('\n', '')
    return answer

if __name__ == '__main__':
    print(transform_answer('The value of the "result" variable at the end is 11.'))
