 # My100DaysOfCode
DAY 1
====================
### Day 1: Introduction to Python
### Author: [ABDULLAHI AHMED OSMAN]
### Date: 2025-01-01
### Description: This is the first day of my 100 days of code challenge. I will begin by introducing myself and explaining the purpose of this challenge.
### Code: This is a simple Python script that prints out a message to the user.# My100DaysOfCode
print("Hello, World!")
print("Welcome to my 100 days of code challenge.")
print("I'm ABDULLAHI ABDULLAHI, and I'm excited to start this journey.")
print("Over the next 100 days, I'll be learning and coding every day.")
print("I'll be sharing my progress and experiences along the way.")
print("Thanks for joining me on this journey!")

DAY 2
====================
### Day 2: Variables and Data Types
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-02
### Description: In this day, I will be learning about variables and data types in Python.
### Code: This is a simple Python script that demonstrates the use of variables and data types.

def variables_and_data_types():
    # Define variables with descriptive names
    full_name = "Abdullahi Ahmed Osman"
    current_age = 21

    # Use f-string formatting for better readability
    print(f"My full name is {full_name} and I am {current_age} years old.")

    # Demonstrate different data types
    print("Data Types in Python:")
    print("1. Integers:", type(current_age))
    print("2. Floats:", type(3.14))
    print("3. Strings:", type(full_name))
    print("4. Boolean:", type(True))
    print("5. List:", type([1, 2, 3]))
    print("6. Tuple:", type((1, 2, 3)))

variables_and_data_types()

DAY 3
====================
### Day 3: Basic Operators
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-03
### Description: In this day, I will be learning about basic operators in Python.
### Code: This is a simple Python script that demonstrates the use of basic operators.

def basic_operators():
    # Define variables
    x = 10
    y = 5

    # Demonstrate arithmetic operators
    print("Arithmetic Operators:")
    print(f"1. Addition: {x} + {y} = {x + y}")
    print(f"2. Subtraction: {x} - {y} = {x - y}")
    print(f"3. Multiplication: {x} * {y} = {x * y}")
    print(f"4. Division: {x} / {y} = {x / y}")

    # Demonstrate comparison operators
    print("\nComparison Operators:")
    print(f"1. Equal to: {x} == {y} = {x == y}")
    print(f"2. Not equal to: {x} != {y} = {x != y}")
    print(f"3. Greater than: {x} > {y} = {x > y}")
    print(f"4. Less than: {x} < {y} = {x < y}")

    # Demonstrate logical operators
    print("\nLogical Operators:")
    print(f"1. And: {x} > 5 and {x} < 15 = {x > 5 and x < 15}")
    print(f"2. Or: {x} > 5 or {x} < 5 = {x > 5 or x < 5}")

basic_operators()

DAY 4
====================
### Day 4: Control Structures
### Author: ABDULLAHI AHMED OSMAN
### Date: 2025-01-04
### Description: In this day, I will be learning about control structures in Python.
### Code: This is a simple Python script that demonstrates the use of control structures.

def control_structures():
    # Define variables
    x = 10
    y = 5

    # Demonstrate if-else statement
    if x > y:  
        print(f"{x} is greater than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is less than {y}")

    # Demonstrate for loop
    print("\nFor Loop:")
    for i in range(5):
        print(i)

    # Demonstrate while loop
    print("\nWhile Loop:")
    i = 0
    while i < 5:
        print(i)
        i += 1

    # Demonstrate nested if-else statement
    print("\nNested If-Else Statement:")
    if x > y:  
        if x > 10:
            print(f"{x} is greater than 10")
        else:
            print(f"{x} is less than or equal to 10")
    else:
        print(f"{x} is less than or equal to {y}")

    # Demonstrate break and continue statements
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

DAY 5
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
 
DAY 6
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



