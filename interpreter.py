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

        # chatgpt often answers this way
        if not answers[index].find('The value of the "result" variable at the end is') == -1:
            answers[index] = answers[index][len('The value of the "result" variable at the end is '):-1]
            ic(answers[index])
            pass
        # strings need to be treated separately (purpose of try catching)
        exec(f"try:\n\tvar = {answers[index]}\nexcept ValueError:\n\tvar = '{answers[index]}'", answer_dict)
        if not answer_dict["var"] == real_answer:
            return False
    return True