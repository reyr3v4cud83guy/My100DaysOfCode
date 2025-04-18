import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import TimeSeriesSplit
import pickle
import warnings
warnings.filterwarnings("ignore")

# Define a function to load the dataset
def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to preprocess the dataset
def preprocess_dataset(dataset):
    try:
        # Drop any rows with missing values
        dataset.dropna(inplace=True)
        
        # Convert categorical variables to numerical variables
        categorical_cols = dataset.select_dtypes(include=['object']).columns
        dataset[categorical_cols] = dataset[categorical_cols].apply(lambda x: pd.factorize(x)[0])
        
        return dataset
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to split the dataset into training and testing sets
def split_dataset(dataset):
    try:
        # Split the dataset into features (X) and target variable (y)
        X = dataset.drop('target', axis=1)
        y = dataset['target']
        
        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to train a linear regression model
def train_model(X_train, y_train):
    try:
        # Create a linear regression model
        model = LinearRegression()
        
        # Train the model
        model.fit(X_train, y_train)
        
        return model
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to evaluate the model
def evaluate_model(model, X_test, y_test):
    try:
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Evaluate the model
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = metrics.r2_score(y_test, y_pred)
        
        print(f"Root Mean Squared Error (RMSE): {rmse}")
        print(f"R-Squared (R2): {r2}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to use cross-validation to evaluate the model
def cross_validate_model(model, X, y):
    try:
        # Use cross-validation to evaluate the model
        scores = cross_val_score(model, X, y, cv=5)
        
        print(f"Cross-Validation Scores: {scores}")
        print(f"Average Cross-Validation Score: {np.mean(scores)}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to use grid search to tune hyperparameters
def tune_hyperparameters(model, X, y):
    try:
        # Define hyperparameter tuning space
        param_grid = {'n_estimators': [10, 50, 100, 200], 'max_depth': [None, 5, 10, 15]}
        
        # Use grid search to tune hyperparameters
        grid_search = GridSearchCV(model, param_grid, cv=5)
        grid_search.fit(X, y)
        
        print(f"Best Parameters: {grid_search.best_params_}")
        print(f"Best Score: {grid_search.best_score_}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to use randomized search to tune hyperparameters
def tune_hyperparameters_randomized(model, X, y):
    try:
        # Define hyperparameter tuning space
        param_grid = {'n_estimators': [10, 50, 100, 200], 'max_depth': [None, 5, 10, 15]}
        
        # Use randomized search to tune hyperparameters
        randomized_search = RandomizedSearchCV(model, param_grid, cv=5, n_iter=10)
        randomized_search.fit(X, y)
        
        print(f"Best Parameters: {randomized_search.best_params_}")
        print(f"Best Score: {randomized_search.best_score_}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to save the model
def save_model(model, file_path):
    try:
        # Save the model
        pickle.dump(model, open(file_path, 'wb'))
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to load the model
def load_model(file_path):
    try:
        # Load the model
        model = pickle.load(open(file_path, 'rb'))
        return model
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Load the dataset
    dataset = load_dataset('lottery_data.csv')
    
    # Preprocess the dataset
    dataset = preprocess_dataset(dataset)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(dataset)
    
    # Train a linear regression model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Use cross-validation to evaluate the model
    cross_validate_model(model, X_train, y_train)
    
    # Use grid search to tune hyperparameters
    tune_hyperparameters(model, X_train, y_train)
    
    # Use randomized search to tune hyperparameters
    tune_hyperparameters_randomized(model, X_train, y_train)
    
    # Save the model
    save_model(model, 'lottery_model.pkl')
    
    # Load the model
    loaded_model = load_model('lottery_model.pkl')
    
    # Use the loaded model to make predictions
    predictions = loaded_model.predict(X_test)
    
    # Print the predictions
    print(predictions)

if __name__ == "__main__":
    main()