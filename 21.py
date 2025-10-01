import random
import time

# Class to represent a single question in the quiz
class Question:
    def __init__(self, question, options, answer, explanation=""):
        self.question = question  # The question text
        self.options = options  # List of possible answers
        self.answer = str(answer)  # Correct answer (as a string)
        self.explanation = explanation  # Explanation for the correct answer

    # Method to ask the question to the user and get their answer
    def ask(self):
        print(self.question)  # Print the question
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")  # Print the options
        start_time = time.time()
        while True:
            user_answer = input("Enter your answer: ")  # Get user input
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(self.options):
                break  # Valid input
            else:
                print("Invalid input. Please enter a number corresponding to the options.")
        end_time = time.time()
        time_taken = end_time - start_time
        if user_answer == self.answer:
            return True, time_taken  # Correct answer
        else:
            return False, time_taken  # Incorrect answer

# Class to represent the quiz
class Quiz:
    def __init__(self):
        self.questions = []  # List to store questions
        self.score = 0  # Initialize score
        self.total_time = 0  # Initialize total time

    # Method to add a question to the quiz
    def add_question(self, question):
        self.questions.append(question)

    # Method to run the quiz
    def run(self):
        random.shuffle(self.questions)  # Shuffle questions
        for question in self.questions:
            correct, time_taken = question.ask()
            self.total_time += time_taken
            if correct:
                self.score += 1  # Increment score for correct answer
                print("Correct!\n")
            else:
                print(f"Sorry, the correct answer is {question.answer}.")
                if question.explanation:
                    print(f"Explanation: {question.explanation}\n")
        print(f"Quiz finished! Your final score is {self.score}/{len(self.questions)}")
        print(f"Total time taken: {self.total_time:.2f} seconds")
        self.save_score()

    # Method to save the score to a file
    def save_score(self):
        with open("quiz_scores.txt", "a") as file:
            file.write(f"Score: {self.score}/{len(self.questions)}, Time: {self.total_time:.2f} seconds\n")

# Main function to set up and run the quiz
def main():
    quiz = Quiz()
    # Adding questions to the quiz
    quiz.add_question(Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "1", "Paris is the capital and most populous city of France."))
    quiz.add_question(Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], "3", "Jupiter is the largest planet in our solar system."))
    quiz.add_question(Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"], "1", "Leonardo da Vinci painted the Mona Lisa."))
    quiz.run()  # Run the quiz

# Entry point of the script
if __name__ == "__main__":
    main()
