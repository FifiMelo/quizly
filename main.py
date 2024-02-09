from question_generator import QuestionGenerator
from explanation_generator import ExplanationGenerator
from fake_answers_generator import FakeAnswersGenerator
from difficulty_estimator import DifficultyEstimator
from tag_creator import TagCreator
from icecream import ic
from puzzle_extractor import extract_puzzle
from dotenv import load_dotenv

import interpreter
import json
import os


def main():
    load_dotenv(override=True)
    batch = list(generate_batch(os.environ.get('TAG')))
    with open("batch.json", "w") as file:
        json.dump(batch, file)



   
    
def generate_complete_puzzle(
        question_generator,
        explanation_generator,
        fake_answers_generator,
        difficulty_estimator,
        tag_creator,
        previous_question = None,
        difficulty_change = 0
            
):
    
    while True:
        original_question = question_generator.generate_question(
            previous_question = previous_question,
            difficulty_change = difficulty_change
            )
        question = extract_puzzle(original_question)
        real_answer, success = interpreter.get_real_answer(question)
        if not success:
            ic(original_question, question)
            continue
        explanator_answer, explanation, explanation_query = explanation_generator.generate_explanation(question)
        difficulty_estimator_answer, difficulty = difficulty_estimator.estimate_difficulty(question)
        

        # place to generate different answers from different bots
        # TODO: update difficulty_change variable
        if type(real_answer) is bool:
            fake_answers = [not real_answer]
        else:
            while True:
                _, fake_answers = fake_answers_generator.generate_fake_answers(question)

                if interpreter.check_answers(
                    real_answer = real_answer,
                    answers = fake_answers,
                    correct_answers = False
                ):
                    break

        answers = [
            explanator_answer,
            #difficulty_estimator_answer
        ]
        if not interpreter.check_answers(
            real_answer = real_answer,
            answers = answers
            ):
            print("Answer of one of the bot seems incorrect")
            ic(question, real_answer, answers, explanation_query)
            continue

        tags = tag_creator.create_tags(question)
        
        return {
                "question": question,
                "real answer": real_answer,
                "explanation": explanation,
                "fake answers": fake_answers,
                "difficulty": difficulty,
                "tags": tags
            }


def generate_batch(tag, n = 5):
    question_generator = QuestionGenerator(os.environ.get('TAG'))
    explanation_generator = ExplanationGenerator()
    fake_answers_generator = FakeAnswersGenerator()
    difficulty_estimator = DifficultyEstimator()
    tag_creator = TagCreator()
    previous_question = None

    for i in range(n):
        puzzle = generate_complete_puzzle(
            question_generator = question_generator,
            explanation_generator = explanation_generator,
            fake_answers_generator = fake_answers_generator,
            difficulty_estimator = difficulty_estimator,
            previous_question = previous_question,
            tag_creator = tag_creator,
            difficulty_change = 1
            
        )
        previous_question = puzzle["question"]
        yield puzzle











if __name__ == '__main__':
    main()




