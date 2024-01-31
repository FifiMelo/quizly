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
            #fake_answers_generator_answer
        ]
        if not interpreter.check_answers(
            real_answer = real_answer,
            answers = answers
            ):
            print("Answer of one of the bot seems incorrect")
            ic(question, real_answer, answers)
            continue

        
        print(real_answer, difficulty_estimator.estimate_difficulty(question))
        with open("puzzle.json", "w") as puzzle:
            json.dump({
                "question": question,
                "real answer": real_answer,
                "explanation": explanation,
                "fake answers": fake_answers
            }, puzzle)
        break


            
    
    








if __name__ == '__main__':
    main()




