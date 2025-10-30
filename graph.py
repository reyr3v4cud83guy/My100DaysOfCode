"""
Graph and Data Visualization Module
Demonstrates the use of various Python modules for data analysis and visualization
Author: Abdullahi .A.Osman
Date: 2025-01-27
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

def demonstrate_modules():
    """Demonstrates the use of various Python modules"""
    print("🐍 Python Modules Demonstration")
    print("=" * 40)
    
    # Math Module
    print("\n📊 Math Module:")
    print(f"  Square root of 16: {math.sqrt(16)}")
    print(f"  Power of 2^3: {math.pow(2, 3)}")
    print(f"  Logarithm of 10: {math.log10(10)}")
    print(f"  Pi value: {math.pi:.4f}")

    # Random Module
    print("\n🎲 Random Module:")
    print(f"  Random integer (1-10): {random.randint(1, 10)}")
    print(f"  Random float (0-1): {random.random():.4f}")
    sample_list = ['apple', 'banana', 'cherry', 'date']
    print(f"  Random choice: {random.choice(sample_list)}")

    # Date and Time Module
    print("\n📅 Date and Time Module:")
    now = datetime.datetime.now()
    print(f"  Current date and time: {now}")
    print(f"  Current date: {datetime.date.today()}")
    print(f"  Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Time Module
    print("\n⏰ Time Module:")
    print(f"  Current timestamp: {time.time():.2f}")
    print(f"  Readable time: {time.ctime()}")

    # OS Module
    print("\n💻 OS Module:")
    print(f"  Operating system: {os.name}")
    print(f"  Current directory: {os.getcwd()}")

    # System Module
    print("\n🖥️ System Module:")
    print(f"  Platform: {sys.platform}")
    print(f"  Python version: {sys.version.split()[0]}")

    # Platform Module
    print("\n🔧 Platform Module:")
    print(f"  System: {platform.system()}")
    print(f"  Machine: {platform.machine()}")

    # Requests Module (with error handling)
    print("\n🌐 Requests Module:")
    try:
        response = requests.get("https://httpbin.org/json", timeout=5)
        print(f"  Status code: {response.status_code}")
        if response.status_code == 200:
            print("  ✅ Request successful")
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Request failed: {e}")

    # JSON Module
    print("\n📄 JSON Module:")
    sample_data = {"name": "Python", "version": "3.9", "type": "language"}
    json_string = json.dumps(sample_data)
    parsed_data = json.loads(json_string)
    print(f"  Original: {sample_data}")
    print(f"  Parsed name: {parsed_data['name']}")

def demonstrate_data_analysis():
    """Demonstrates data analysis with pandas and numpy"""
    print("\n📈 Data Analysis Demonstration")
    print("=" * 40)
    
    # Pandas Module
    print("\n🐼 Pandas Module:")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Tokyo', 'Paris'],
        'Salary': [50000, 60000, 70000, 55000]
    }
    df = pd.DataFrame(data)
    print(f"  Dataset shape: {df.shape}")
    print(f"  Average age: {df['Age'].mean():.1f}")
    print(f"  Max salary: ${df['Salary'].max():,}")
    
    # NumPy Module
    print("\n🔢 NumPy Module:")
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"  Array: {array}")
    print(f"  Mean: {np.mean(array):.2f}")
    print(f"  Standard deviation: {np.std(array):.2f}")
    print(f"  Sum: {np.sum(array)}")
    
    return df, array

def create_visualizations(df, array):
    """Creates sample visualizations"""
    print("\n📊 Creating Visualizations...")
    
    try:
        # Set style
        plt.style.use('default')
        
        # Create a simple plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Bar plot
        ax1.bar(df['Name'], df['Age'])
        ax1.set_title('Age by Person')
        ax1.set_xlabel('Name')
        ax1.set_ylabel('Age')
        ax1.tick_params(axis='x', rotation=45)
        
        # Line plot
        ax2.plot(array, marker='o')
        ax2.set_title('Array Values')
        ax2.set_xlabel('Index')
        ax2.set_ylabel('Value')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        print("  ✅ Matplotlib visualizations created!")
        
        # Seaborn example
        sns.set_style("whitegrid")
        plt.figure(figsize=(8, 6))
        sns.barplot(data=df, x='Name', y='Salary')
        plt.title('Salary by Person')
        plt.xticks(rotation=45)
        plt.show()
        
        print("  ✅ Seaborn visualization created!")
        
        # Plotly example
        fig = go.Figure(data=[
            go.Scatter(x=df['Name'], y=df['Salary'], 
                      mode='markers+lines', name='Salary',
                      marker=dict(size=10, color='blue'))
        ])
        fig.update_layout(
            title='Interactive Salary Chart',
            xaxis_title='Name',
            yaxis_title='Salary ($)'
        )
        fig.show()
        
        print("  ✅ Plotly interactive chart created!")
        
    except Exception as e:
        print(f"  ⚠️ Visualization error: {e}")
        print("  Note: Ensure display is available for matplotlib")

def main():
    """Main function to run all demonstrations"""
    print("🚀 Starting Python Modules and Visualization Demo")
    print("=" * 50)
    
    # Demonstrate basic modules
    demonstrate_modules()
    
    # Demonstrate data analysis
    df, array = demonstrate_data_analysis()
    
    # Create visualizations
    create_visualizations(df, array)
    
    print("\n✨ Demo completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()