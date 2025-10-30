"""
Test script to verify all required packages are installed correctly
Run this to check if your environment is set up properly
"""

def test_imports():
    """Test all required imports"""
    print("🧪 Testing Python Package Imports...")
    print("=" * 50)
    
    try:
        import pandas as pd
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ matplotlib imported successfully")
    except ImportError as e:
        print(f"❌ matplotlib import failed: {e}")
        return False
    
    try:
        import seaborn as sns
        print("✅ seaborn imported successfully")
    except ImportError as e:
        print(f"❌ seaborn import failed: {e}")
        return False
    
    try:
        import plotly.graph_objects as go
        print("✅ plotly imported successfully")
    except ImportError as e:
        print(f"❌ plotly import failed: {e}")
        return False
    
    try:
        import requests
        print("✅ requests imported successfully")
    except ImportError as e:
        print(f"❌ requests import failed: {e}")
        return False
    
    try:
        from sklearn.ensemble import RandomForestRegressor
        print("✅ scikit-learn imported successfully")
    except ImportError as e:
        print(f"❌ scikit-learn import failed: {e}")
        return False
    
    # Test basic functionality
    print("\n🔬 Testing Basic Functionality...")
    print("-" * 30)
    
    try:
        # Test pandas
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print(f"✅ pandas DataFrame created: {df.shape}")
        
        # Test numpy
        arr = np.array([1, 2, 3, 4, 5])
        print(f"✅ numpy array created: {arr.shape}")
        
        # Test basic math
        mean_val = np.mean(arr)
        print(f"✅ numpy calculation: mean = {mean_val}")
        
        print("\n🎉 All tests passed! Your environment is ready.")
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    if success:
        print("\n✨ You can now run your Python projects without import errors!")
    else:
        print("\n⚠️ Some issues detected. Please check the error messages above.")