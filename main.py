from question_generator import QuestionGenerator
from explanation_generator import ExplanationGenerator
from fake_answers_generator import FakeAnswersGenerator
from difficulty_estimator import DifficultyEstimator
from icecream import ic
from puzzle_extractor import extract_puzzle
from dotenv import load_dotenv
import interpreter
import json
import os


def main():

    load_dotenv()
    # initialization of bots
    question_generator = QuestionGenerator(os.environ.get('TAG'))
    explanation_generator = ExplanationGenerator()
    fake_answers_generator = FakeAnswersGenerator()
    difficulty_estimator = DifficultyEstimator()


    # creating question
    puzzle = generate_complete_puzzle(
        question_generator = question_generator,
        explanation_generator = explanation_generator,
        fake_answers_generator = fake_answers_generator,
        difficulty_estimator = difficulty_estimator
    )
    print("Final puzzle")
    ic(puzzle)
    with open("puzzle.json", "w") as f:
        json.dump(puzzle, f)

   
    
def generate_complete_puzzle(
        question_generator,
        explanation_generator,
        fake_answers_generator,
        difficulty_estimator,
        difficulty_change = 0     
):
    
    while True:
        original_question = question_generator.generate_question(difficulty_change = difficulty_change)
        question = extract_puzzle(original_question)
        real_answer, success = interpreter.get_real_answer(question)
        if not success:
            ic(original_question, question)
            continue
        explanator_answer, explanation = explanation_generator.generate_explanation(question)
        difficulty_estimator_answer, difficulty = difficulty_estimator.estimate_difficulty(question)
        

        # place to generate different answers from different bots
        # TODO: update difficulty_change variable


        while True:
            _, fake_answers = fake_answers_generator.generate_fake_answers(question)

            if interpreter.check_answers(
                real_answer = real_answer,
                answers = fake_answers,
                correct_answers = False
            ):
                break
            print("One of the fake answers seems to be correct, creating new fake answers")
            ic(question, real_answer, fake_answers)

        answers = [
            explanator_answer,
            difficulty_estimator_answer
        ]
        if not interpreter.check_answers(
            real_answer = real_answer,
            answers = answers
            ):
            print("Answer of one of the bot seems incorrect")
            ic(question, real_answer, answers)
            continue
        
        return {
                "question": question,
                "real answer": real_answer,
                "explanation": explanation,
                "fake answers": fake_answers,
                "difficulty": difficulty
            }


    









if __name__ == '__main__':
    main()




