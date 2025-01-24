  my_branch
import random

def game():
    while True:
        user = input("Enter a choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user == "quit":
            break
        elif user not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer = random.choice(["rock", "paper", "scissors"])
        print(f"\nYou chose {user}, computer chose {computer}.\n")

        if user == computer:
            print(f"Both players selected {user}. It's a tie!")
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

=======
import random

def game():
    while True:
        user = input("Enter a choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user == "quit":
            break
        elif user not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer = random.choice(["rock", "paper", "scissors"])
        print(f"\nYou chose {user}, computer chose {computer}.\n")

        if user == computer:
            print(f"Both players selected {user}. It's a tie!")
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

  Osman--branch
game()