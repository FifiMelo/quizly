from question_generator import QuestionGenerator
from explanation_generator import ExplanationGenerator
from puzzle import Puzzle
from icecream import ic

def main():

    question_generator = QuestionGenerator("modulo operator")
    explanation_generator = ExplanationGenerator()
    question = question_generator.generate_question()
    answer, explanation = explanation_generator.generate_explanation(question)
    ic(question)
    ic(answer, explanation)




if __name__ == '__main__':
    main()




