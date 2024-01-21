from question_generator import QuestionGenerator
from puzzle import Puzzle

def main():
    question_generator = QuestionGenerator("2d arrays")
    print(question_generator.generate())
    print(question_generator.generate(1))
    print(question_generator.generate(-1))



if __name__ == '__main__':
    main()




