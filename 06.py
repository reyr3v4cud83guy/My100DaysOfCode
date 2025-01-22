import math
import random
import datetime
import time
import os
import sys
import platform
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import requests

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
    try:
        print("Requests Module:")
        response = requests.get("https://www.example.com")
        print("Status code:", response.status_code)
        print("Response headers:", response.headers)
        print("Response content:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
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
    plt.figure(figsize=(10, 6))
    plt.plot([1, 2, 3, 4, 5])
    plt.title("Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()
    print("Seaborn Module:")
    sns.set()
    plt.figure(figsize=(10, 6))
    plt.plot([1, 2, 3, 4, 5])
    plt.title("Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()
    print("Plotly Module:")
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])])
    fig.update_layout(title="Line Plot", xaxis_title="X-axis", yaxis_title="Y-axis")
    fig.show()

def main():
    modules_example()

if __name__ == "__main__":
    main()
