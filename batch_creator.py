from question_generator import QuestionGenerator
from explanation_generator import ExplanationGenerator
from fake_answers_generator import FakeAnswersGenerator
from difficulty_estimator import DifficultyEstimator
from tag_creator import TagCreator

from puzzle_extractor import extract_puzzle
import interpreter


   
    
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










def generate_batch(tag, n = 100):
    question_generator = QuestionGenerator(tag)
    explanation_generator = ExplanationGenerator()
    fake_answers_generator = FakeAnswersGenerator()
    difficulty_estimator = DifficultyEstimator()
    tag_creator = TagCreator()
    previous_question = None
    difficulty_change = 0



    for i in range(n):
        puzzle = generate_complete_puzzle(
            question_generator = question_generator,
            explanation_generator = explanation_generator,
            fake_answers_generator = fake_answers_generator,
            difficulty_estimator = difficulty_estimator,
            previous_question = previous_question,
            tag_creator = tag_creator,
            difficulty_change = difficulty_change
            
        )

        difficulty = puzzle["difficulty"]
        if difficulty < 40:
            difficulty_change = 1
        elif difficulty > 80:
            difficulty_change = -1
        else:
            difficulty_change = 0

        previous_question = puzzle["question"]
        yield puzzle