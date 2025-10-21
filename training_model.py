import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn import metrics 
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import GridSearchCV 
from sklearn.model_selection import RandomizedSearchCV 
from sklearn.ensemble import RandomForestRegressor 
import pickle
import numpy as np 

def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except Exception as e:
        print(f"An error occurred: {e}")

def preprocess_dataset(dataset):
    try:
        dataset.dropna(inplace=True)
        categorical_cols = dataset.select_dtypes(include=['object']).columns
        dataset[categorical_cols] = dataset[categorical_cols].apply(lambda x: pd.factorize(x)[0])
        return dataset
    except Exception as e:
        print(f"An error occurred: {e}")

def split_dataset(dataset):
    try:
        X = dataset.drop('target', axis=1)
        y = dataset['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"An error occurred: {e}")

def train_model(X_train, y_train):
    try:
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"An error occurred: {e}")

def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = metrics.r2_score(y_test, y_pred)
        print(f"Root Mean Squared Error (RMSE): {rmse}")
        print(f"R-Squared (R2): {r2}")
    except Exception as e:
        print(f"An error occurred: {e}")

def cross_validate_model(model, X, y):
    try:
        scores = cross_val_score(model, X, y, cv=5)
        print(f"Cross-Validation Scores: {scores}")
        print(f"Average Cross-Validation Score: {np.mean(scores)}")
    except Exception as e:
        print(f"An error occurred: {e}")

def tune_hyperparameters(model, X, y):
    try:
        param_grid = {'n_estimators': [10, 50, 100, 200], 'max_depth': [None, 5, 10, 15]}
        grid_search = GridSearchCV(model, param_grid, cv=5)
        grid_search.fit(X, y)
        print(f"Best Parameters: {grid_search.best_params_}")
        print(f"Best Score: {grid_search.best_score_}")
        return grid_search.best_estimator_
    except Exception as e:
        print(f"An error occurred: {e}")

def tune_hyperparameters_randomized(model, X, y):
    try:
        param_grid = {'n_estimators': [10, 50, 100, 200], 'max_depth': [None, 5, 10, 15]}
        randomized_search = RandomizedSearchCV(model, param_grid, cv=5, n_iter=10)
        randomized_search.fit(X, y)
        print(f"Best Parameters: {randomized_search.best_params_}")
        print(f"Best Score: {randomized_search.best_score_}")
        return randomized_search.best_estimator_
    except Exception as e:
        print(f"An error occurred: {e}")

def save_model(model, file_path):
    try:
        pickle.dump(model, open(file_path, 'wb'))
    except Exception as e:
        print(f"An error occurred: {e}")

def load_model(file_path):
    try:
        model = pickle.load(open(file_path, 'rb'))
        return model
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    dataset = load_dataset('lottery_data.csv')
    dataset = preprocess_dataset(dataset)
    X_train, X_test, y_train, y_test = split_dataset(dataset)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    cross_validate_model(model, X_train, y_train)
    best_model = tune_hyperparameters(model, X_train, y_train)
    best_model_randomized = tune_hyperparameters_randomized(model, X_train, y_train)
    save_model(best_model, 'lottery_model.pkl')
    loaded_model = load_model('lottery_model.pkl')

if __name__ == "__main__":
    main()