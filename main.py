from question_generator import QuestionGenerator
from explanation_generator import ExplanationGenerator
from puzzle import Puzzle
from icecream import ic
from puzzle_extractor import extract_puzzle
from interpreter import get_real_answer

def main():
    # initialization of bots
    question_generator = QuestionGenerator("arithmetics")
    explanation_generator = ExplanationGenerator()

    # creating question
    question = question_generator.generate_question()
    question = extract_puzzle(question)

    explanator_answer, explanation = explanation_generator.generate_explanation(question)
    real_answer, success = get_real_answer(question)

    ic(question, explanator_answer, real_answer, success, explanation)
    








if __name__ == '__main__':
    main()




