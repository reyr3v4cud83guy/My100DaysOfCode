"""

Enhanced Graph and Data Visualization Module

Demonstrates the use of various Python modules for data analysis and visualization
"""


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


def demonstrate_math_module():

    """Demonstrates mathematical operations using the math module"""

    print("📊 Math Module:"
)
    print(f"  Square root of 16: {math.sqrt(16)}")

    print(f"  Power of 2^3: {math.pow(2, 3)}")

    print(f"  Logarithm of 10: {math.log10(10)}")

    print(f"  Sine of π/2: {math.sin(math.pi/2)}")

    print(f"  Factorial of 5: {math.factorial(5)}")

def demonstrate_random_module():

    """Demonstrates random number generation"""

    print("\n🎲 Random Module:"
)
    print(f"  Random integer (1-10): {random.randint(1, 10)}")

    print(f"  Random float (0-1): {random.random():.4f}")

    print(f"  Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")
    

    # Generate sample data for visualization

    sample_data = [random.randint(1, 100) for _ in range(10)]

    print(f"  Sample data: {sample_data}")
    return sample_data

def demonstrate_datetime_module():

    """Demonstrates date and time operations"""

    print("\n📅 Date and Time Module:"
)
    now = datetime.datetime.now()

    print(f"  Current date and time: {now}")

    print(f"  Current date: {datetime.date.today()}")

    print(f"  Current time: {now.time()}")

    print(f"  Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def demonstrate_system_modules():

    """Demonstrates system information modules"""

    print("\n💻 System Information:"
)
    print(f"  Operating system: {os.name}")

    print(f"  Current directory: {os.getcwd()}")

    print(f"  Platform: {sys.platform}")

    print(f"  Python version: {sys.version.split()[0]}")

    print(f"  System platform: {platform.platform()}")


def demonstrate_web_requests():
    """Demonstrates web requests (with error handling)"""
    print("\n🌐 Web Requests Module:")
    try:

        response = requests.get("https://httpbin.org/json", timeout=5)

        print(f"  Status code: {response.status_code}")

        print(f"  Response time: {response.elapsed.total_seconds():.2f}s")

        if response.status_code == 200:

            data = response.json()

            print(f"  Sample data received: {list(data.keys())}")

    except requests.exceptions.RequestException as e:

        print(f"  Request failed: {e}")


def demonstrate_json_module():

    """Demonstrates JSON operations"""

    print("\n📄 JSON Module:"
)
    sample_data = {

        "name": "Python Data Analysis",

        "version": "1.0",

        "modules": ["pandas", "numpy", "matplotlib"],

        "active": True

    }
    

    json_string = json.dumps(sample_data, indent=2)

    print(f"  JSON string created: {len(json_string)} characters")
    

    parsed_data = json.loads(json_string)

    print(f"  Parsed data - Name: {parsed_data['name']}")

    print(f"  Modules count: {len(parsed_data['modules'])}")

def demonstrate_pandas_module():

    """Demonstrates pandas data manipulation"""

    print("\n🐼 Pandas Module:")
    

    # Create sample dataset

    data = {

        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],

        'Age': [25, 30, 35, 28, 32],

        'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],

        'Salary': [50000, 60000, 70000, 55000, 65000]

    }
    

    df = pd.DataFrame(data)

    print(f"  Dataset shape: {df.shape}")

    print(f"  Average age: {df['Age'].mean():.1f}")

    print(f"  Average salary: ${df['Salary'].mean():,.0f}")

    print(f"  Cities: {', '.join(df['City'].unique())}")
    
    return df

def demonstrate_numpy_module():

    """Demonstrates numpy array operations"""

    print("\n🔢 NumPy Module:")
    

    # Create arrays

    array1 = np.array([1, 2, 3, 4, 5])

    array2 = np.random.randint(1, 10, 5)
    

    print(f"  Array 1: {array1}")

    print(f"  Array 2: {array2}")

    print(f"  Sum: {np.sum(array1)}")

    print(f"  Mean: {np.mean(array1):.2f}")

    print(f"  Standard deviation: {np.std(array1):.2f}")

    print(f"  Element-wise addition: {array1 + array2}")
    

    return array1, array2




def create_visualizations(sample_data, df, arrays):

    """Creates various visualizations using matplotlib, seaborn, and plotly"""

    print("\n📈 Creating Visualizations...")
    

    # Set style for better-looking plots

    plt.style.use('seaborn-v0_8')

    sns.set_palette("husl")
    

    # Create matplotlib visualization

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    fig.suptitle('Data Visualization Examples', fontsize=16)
    

    # Line plot

    axes[0, 0].plot(sample_data, marker='o')

    axes[0, 0].set_title('Random Data Line Plot')

    axes[0, 0].set_xlabel('Index')

    axes[0, 0].set_ylabel('Value')

    axes[0, 0].grid(True, alpha=0.3)
    

    # Bar plot

    axes[0, 1].bar(df['Name'], df['Age'])

    axes[0, 1].set_title('Age by Person')

    axes[0, 1].set_xlabel('Name')

    axes[0, 1].set_ylabel('Age')

    axes[0, 1].tick_params(axis='x', rotation=45)
    

    # Histogram

    axes[1, 0].hist(sample_data, bins=5, alpha=0.7, edgecolor='black')

    axes[1, 0].set_title('Data Distribution')

    axes[1, 0].set_xlabel('Value')

    axes[1, 0].set_ylabel('Frequency')
    

    # Scatter plot

    x_data = np.random.randn(50)

    y_data = x_data + np.random.randn(50) * 0.5

    axes[1, 1].scatter(x_data, y_data, alpha=0.6)

    axes[1, 1].set_title('Scatter Plot')

    axes[1, 1].set_xlabel('X values')

    axes[1, 1].set_ylabel('Y values')
    

    plt.tight_layout()

    plt.show()
    

    # Create plotly interactive visualization

    fig_plotly = go.Figure()

    fig_plotly.add_trace(go.Scatter(

        x=df['Name'], 

        y=df['Salary'],

        mode='markers+lines',

        name='Salary',

        marker=dict(size=10, color=df['Age'], colorscale='Viridis', showscale=True)
    ))
    

    fig_plotly.update_layout(

        title='Interactive Salary vs Name (Color by Age)',

        xaxis_title='Name',

        yaxis_title='Salary ($)',

        hovermode='closest'
    )
    

    fig_plotly.show()
    

    print("  ✅ Visualizations created successfully!")

def main():

    """Main function to demonstrate all modules"""

    print("🚀 Python Modules Demonstration")
    print("=" * 50)
    

    # Demonstrate various modules

    demonstrate_math_module()

    sample_data = demonstrate_random_module()
    demonstrate_datetime_module()
    demonstrate_system_modules()

    demonstrate_web_requests()

    demonstrate_json_module()

    df = demonstrate_pandas_module()

    arrays = demonstrate_numpy_module()
    

    # Create visualizations
    try:

        create_visualizations(sample_data, df, arrays)

    except Exception as e:

        print(f"  ⚠️ Visualization error: {e}")

        print("  Note: Make sure you have a display available for matplotlib")
    

    print("\n✨ Module demonstration completed!")

    print("=" * 50)


if __name__ == "__main__":
    main()