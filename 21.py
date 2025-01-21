import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer: ")
        if user_answer == self.answer:
            return True
        else:
            return False

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        for question in self.questions:
            if question.ask():
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Sorry, the correct answer is {question.answer}.\n")
        print(f"Quiz finished! Your final score is {self.score}/{len(self.questions)}")

def main():
    quiz = Quiz()
    quiz.add_question(Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "1"))
    quiz.add_question(Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], "3"))
    quiz.add_question(Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"], "1"))
    quiz.run()

if __name__ == "__main__":
    main()
 