from icecream import ic


def answers_correct(real_answer, answers):
    """
    Answers from chatgpt will always come as strings, but they can represent all posiible
    types, numbers, arrays, dictionaries ect.
    Purpose of this function is to compare these answers, 
    and return True only if all of them are correct.
    """
    answer_dict = dict()
    for answer in answers:
        try:
            exec(f"var = {answer}", answer_dict)
        except NameError:
            exec(f"var = '{answer}'", answer_dict)
        if not answer_dict["var"] == real_answer:
            return False
    return True
    

if __name__ == "__main__":
    print(answers_correct(3, ["3", "3 "]))