from random import random
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor 
from sklearn import metrics 
import pickle
import sys
import os

# --- Configuration ---
TARGET_COLUMN = 'target_value'
MODEL_FILENAME = 'lottery_model.pkl'

def create_dummy_dataset():
    """
    Creates a dummy dataset for demonstration since 'lottery_data.csv' is unavailable.
    REMOVE THIS FUNCTION when using your real data file.
    """
    print("WARNING: Using dummy dataset. Replace 'create_dummy_dataset' call with 'load_dataset('your_file.csv')' for real use.")
    data = {
        'feature_A': np.random.rand(100) * 10,
        'feature_B': np.random.randint(0, 5, 100),
        'feature_C_cat': [random.choice(['A', 'B', 'C']) for _ in range(100)],
        TARGET_COLUMN: np.random.rand(100) * 100  # Our target variable
    } 
    return pd.DataFrame(data)

def load_dataset(file_path):
    """Loads dataset from file path."""
    try:
        dataset = pd.read_csv(file_path)
        print(f"Dataset loaded successfully from: {file_path}")
        return dataset
    except FileNotFoundError:
        print(f"Error: Dataset file not found at '{file_path}'.")
        return None
    except Exception as e:
        print(f"An error occurred during loading: {e}")
        return None

def preprocess_dataset(dataset):
    """Handles missing values and encodes categorical columns."""
    if dataset is None:
        return None
        
    try:
        # 1. Handle missing values
        dataset.dropna(inplace=True)
        
        # 2. Encode categorical features using factorize
        categorical_cols = dataset.select_dtypes(include=['object']).columns
        if not categorical_cols.empty:
            print(f"Encoding categorical columns: {list(categorical_cols)}")
            # Apply factorize, which returns a tuple (encoded_array, unique_labels)
            dataset[categorical_cols] = dataset[categorical_cols].apply(lambda x: pd.factorize(x)[0])
        
        return dataset
    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")
        return None

def split_dataset(dataset, target_column):
    """Splits features (X) and target (y) into training and testing sets."""
    if dataset is None or target_column not in dataset.columns:
        print(f"Error: Cannot split dataset. Target column '{target_column}' is missing or dataset is invalid.")
        return None, None, None, None
        
    try:
        X = dataset.drop(target_column, axis=1)
        y = dataset[target_column]
        print(f"Splitting data: X shape={X.shape}, y shape={y.shape}")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"An error occurred during splitting: {e}")
        return None, None, None, None

def train_model(X_train, y_train):
    """Trains a Random Forest Regressor model."""
    try:
        model = RandomForestRegressor(random_state=42)
        print("Starting model training (RandomForestRegressor)...")
        model.fit(X_train, y_train)
        print("Training complete.")
        return model
    except Exception as e:
        print(f"An error occurred during training: {e}")
        return None

def evaluate_model(model, X_test, y_test):
    """Evaluates the model using RMSE and R-Squared metrics."""
    if model is None:
        return
    try:
        y_pred = model.predict(X_test)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = metrics.r2_score(y_test, y_pred)
        print("\n--- Model Evaluation ---")
        print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
        print(f"R-Squared (R2): {r2:.4f}")
    except Exception as e:
        print(f"An error occurred during evaluation: {e}")

def cross_validate_model(model, X, y):
    """Performs 5-fold cross-validation."""
    if model is None:
        return
    try:
        print("\n--- Cross Validation (5-fold) ---")
        scores = cross_val_score(model, X, y, cv=5, scoring='r2')
        print(f"Cross-Validation Scores (R2): {scores}")
        print(f"Average Cross-Validation Score: {np.mean(scores):.4f}")
    except Exception as e:
        print(f"An error occurred during cross-validation: {e}")

def tune_hyperparameters(model, X, y):
    """Tunes hyperparameters using GridSearchCV."""
    if model is None:
        return None
    try:
        print("\n--- Hyperparameter Tuning (Grid Search) ---")
        # Simplified param_grid for Random Forest
        param_grid = {
            'n_estimators': [50, 100], 
            'max_depth': [5, 10]
        }
        grid_search = GridSearchCV(model, param_grid, cv=3, scoring='r2', verbose=1, n_jobs=-1)
        grid_search.fit(X, y)
        print(f"Best Parameters: {grid_search.best_params_}")
        print(f"Best R2 Score: {grid_search.best_score_:.4f}")
        return grid_search.best_estimator_
    except Exception as e:
        print(f"An error occurred during Grid Search tuning: {e}")
        return None

def tune_hyperparameters_randomized(model, X, y):
    """Tunes hyperparameters using RandomizedSearchCV."""
    if model is None:
        return None
    try:
        print("\n--- Hyperparameter Tuning (Randomized Search) ---")
        param_grid = {
            'n_estimators': [10, 50, 100, 200], 
            'max_depth': [None, 5, 10, 15]
        }
        # Reducing n_iter for quick testing
        randomized_search = RandomizedSearchCV(model, param_grid, cv=3, n_iter=5, scoring='r2', verbose=1, n_jobs=-1, random_state=42)
        randomized_search.fit(X, y)
        print(f"Best Parameters: {randomized_search.best_params_}")
        print(f"Best R2 Score: {randomized_search.best_score_:.4f}")
        return randomized_search.best_estimator_
    except Exception as e:
        print(f"An error occurred during Randomized Search tuning: {e}")
        return None

def save_model(model, file_path):
    """Saves the trained model using pickle."""
    if model is None:
        return
    try:
        print(f"\nSaving model to {file_path}...")
        pickle.dump(model, open(file_path, 'wb'))
        print("Model saved successfully.")
    except Exception as e:
        print(f"An error occurred during model saving: {e}")

def load_model(file_path):
    """Loads the trained model using pickle."""
    try:
        print(f"Loading model from {file_path}...")
        model = pickle.load(open(file_path, 'rb'))
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print(f"Error: Model file not found at '{file_path}'.")
        return None
    except Exception as e:
        print(f"An error occurred during model loading: {e}")
        return None

def main():
    # 1. Data Loading (Using dummy data for immediate execution)
    # If you have your file, uncomment the line below and comment out the dummy call:
    # dataset = load_dataset('lottery_data.csv')
    dataset = create_dummy_dataset()
    
    if dataset is None:
        print("Exiting pipeline due to failed data loading.")
        return

    # 2. Preprocessing
    dataset = preprocess_dataset(dataset)
    if dataset is None:
        print("Exiting pipeline due to failed preprocessing.")
        return

    # 3. Splitting
    X_train, X_test, y_train, y_test = split_dataset(dataset, TARGET_COLUMN)
    if X_train is None:
        print("Exiting pipeline due to failed data splitting.")
        return

    # 4. Training
    model = train_model(X_train, y_train)
    if model is None:
        print("Exiting pipeline due to failed model training.")
        return
        
    # 5. Evaluation and Cross-Validation
    evaluate_model(model, X_test, y_test)
    cross_validate_model(model, X_train, y_train)
    
    # 6. Hyperparameter Tuning
    best_model = tune_hyperparameters(model, X_train, y_train)
    best_model_randomized = tune_hyperparameters_randomized(model, X_train, y_train)

    # 7. Model Saving and Loading
    # We save the best model found by GridSearchCV
    if best_model is not None:
        save_model(best_model, MODEL_FILENAME)
        loaded_model = load_model(MODEL_FILENAME)
        
        # Verify loaded model
        if loaded_model is not None:
             print("\nLoaded model verification:")
             evaluate_model(loaded_model, X_test, y_test)


if __name__ == "__main__":
    main()
