from question_generator import QuestionGenerator
from explanation_generator import ExplanationGenerator
from puzzle import Puzzle
from icecream import ic
from puzzle_extractor import extract_puzzle
import interpreter
import json

def main():
    # initialization of bots
    question_generator = QuestionGenerator("arrays")
    explanation_generator = ExplanationGenerator()

    difficulty_change = 0
    # creating question
    while True:
        original_question = question_generator.generate_question(difficulty_change = difficulty_change)
        question = extract_puzzle(original_question)
        real_answer, success = interpreter.get_real_answer(question)
        if not success:
            ic(original_question, question)
            continue
        explanator_answer, explanation = explanation_generator.generate_explanation(question)

        # place to generate different answers from different bots
        # and to update difficulty_change variable


        answers = [
            explanator_answer
        ]
        if not interpreter.answers_correct(
            real_answer = real_answer,
            answers = answers
            ):

            ic(question, real_answer, answers)
            continue
    
        with open("puzzle.json", "w") as puzzle:
            json.dump({
                "question": question,
                "real answer": real_answer,
                "explanation": explanation
            }, puzzle)
        break

            
    
    








if __name__ == '__main__':
    main()




