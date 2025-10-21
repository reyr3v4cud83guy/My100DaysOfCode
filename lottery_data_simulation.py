import csv
import warnings
import random
import math
import sys
import os
import numpy as np # <-- CRITICAL: Added numpy import for array operations and math
warnings.filterwarnings("ignore")

# Configuration (Define your target column name here)
TARGET_COLUMN = 'target'
DATA_FILENAME = 'lottery_data.csv'

def create_dummy_dataset():
    """
    Creates a simple dummy dataset for testing since the CSV file is not present.
    This simulates numeric lottery data with a 'target' column.
    """
    print(f"WARNING: File '{DATA_FILENAME}' not found. Generating dummy dataset.")
    header = ['draw_date', 'num1', 'num2', 'num3', 'num4', 'num5', TARGET_COLUMN]
    data = []
    for _ in range(50): # 50 rows of data
        # Example data: date string, 5 lottery numbers (1-50), and a target (51-100)
        row = [f"2023-01-{_+1:02d}"]
        row.extend([str(random.randint(1, 50)) for _ in range(5)])
        row.append(str(random.randint(51, 100)))
        data.append(row)
    return header, data

def load_dataset(file_path):
    """Loads dataset from file path or generates dummy data if not found."""
    try:
        if not os.path.exists(file_path):
            return create_dummy_dataset()
            
        # FIX: Ensure all file reading and initial assignments are within the try block
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        if not data:
            print("Error: CSV file is empty.")
            return None, None

        header = [h.strip() for h in data[0]] # Clean header
        dataset = data[1:]
        print(f"Dataset loaded successfully with {len(dataset)} rows.")
        return header, dataset
    except Exception as e:
        print(f"An error occurred during loading: {e}")
        return None, None

def preprocess_dataset(header, dataset):
    """Handles preprocessing including missing values, outliers, encoding, and feature engineering."""
    try:
        if header is None or dataset is None:
            return None, None

        print("\n--- Preprocessing Steps ---")

        # 1. Drop any rows with missing values
        initial_count = len(dataset)
        dataset = [row for row in dataset if all(row)]
        print(f"Dropped {initial_count - len(dataset)} rows with missing values.")

        # 2. Identify column types and convert numeric values to float
        numeric_cols_indices = []
        categorical_cols_indices = []
        
        # Determine column types
        for col_index, col_name in enumerate(header):
            # Check if at least one value is non-numeric
            if any(True for row in dataset if not row[col_index].replace('.', '', 1).isdigit()):
                 categorical_cols_indices.append(col_index)
            else:
                numeric_cols_indices.append(col_index)

        # Convert and apply basic outlier removal (0-100 range)
        temp_data = []
        for row in dataset:
            new_row = []
            is_outlier_row = False
            for i, val_str in enumerate(row):
                if i in numeric_cols_indices:
                    try:
                        val = float(val_str)
                        if val < 0 or val > 100:
                            is_outlier_row = True
                        new_row.append(val)
                    except ValueError:
                        # Should not happen, but treat as string fallback
                        new_row.append(val_str)
                else:
                    new_row.append(val_str)
            if not is_outlier_row:
                temp_data.append(new_row)
        
        dataset = temp_data
        print(f"Remaining rows after cleaning/outlier removal: {len(dataset)}")

        # 3. Handle categorical columns (Dropping for simplicity with date/ID)
        new_header = list(header)
        
        if categorical_cols_indices:
            print(f"Dropping column(s): {[header[i] for i in categorical_cols_indices]}")
            # Drop categorical columns
            # Iterate backwards to safely pop multiple indices
            for index in sorted(categorical_cols_indices, reverse=True):
                new_header.pop(index)
                dataset = [row[:index] + row[index+1:] for row in dataset]

        # Re-identify numeric indices after dropping columns
        # Now, all columns are numeric OR the target.
        numeric_cols_indices = [i for i, col in enumerate(new_header) if col != TARGET_COLUMN]
        
        # 4. Feature engineering: add sum and average of lottery numbers
        new_header += ['numbers_sum', 'numbers_avg']
        
        for row in dataset:
            # Convert all non-target, non-dropped values to float for engineering
            nums_to_sum = []
            for i, val in enumerate(row):
                if i in numeric_cols_indices:
                    nums_to_sum.append(float(val)) # Data is still strings/floats mix here

            row.append(sum(nums_to_sum))
            row.append(sum(nums_to_sum) / len(nums_to_sum) if nums_to_sum else 0)

        # 5. Normalization (Min-Max Scaling using NumPy)
        # Convert all data to floats for final processing
        processed_dataset = [[float(val) for val in row] for row in dataset]

        data_np = np.array(processed_dataset)
        min_vals = data_np.min(axis=0)
        max_vals = data_np.max(axis=0)
        
        # Avoid division by zero by setting range to 1.0 if min == max
        ranges = max_vals - min_vals
        ranges[ranges == 0] = 1.0 
        
        # Perform normalization
        processed_dataset = (data_np - min_vals) / ranges
        processed_dataset = processed_dataset.tolist()
        
        print("Preprocessing complete.")
        return new_header, processed_dataset
        
    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")
        return None, None

# Define a function to split the dataset into training and testing sets
def split_dataset(header, dataset, test_size=0.2):
    """Splits the dataset into training and testing sets."""
    try:
        if header is None or dataset is None:
            return None, None, None, None
            
        target_index = header.index(TARGET_COLUMN)
        
        # Split the dataset into features (X) and target variable (y)
        # X: all columns except target. y: only the target column.
        X = [row[:target_index] + row[target_index+1:] for row in dataset]
        y = [row[target_index] for row in dataset]
        
        # Data is already guaranteed to be float/int by preprocess_dataset
        
        # Shuffle (safe to do again)
        combined = list(zip(X, y))
        random.shuffle(combined)
        X, y = zip(*combined)
        
        # Split the dataset into training and testing sets based on index
        split_index = int(len(X) * (1 - test_size))
        X_train, X_test = list(X[:split_index]), list(X[split_index:])
        y_train, y_test = list(y[:split_index]), list(y[split_index:])
        
        print(f"Data split: Train={len(X_train)}, Test={len(X_test)}")
        
        return X_train, X_test, y_train, y_test
    except ValueError as e:
        print(f"Error: Target column '{TARGET_COLUMN}' not found in header. {e}")
        return None, None, None, None
    except Exception as e:
        print(f"An error occurred during splitting: {e}")
        return None, None, None, None

# Main function
def main():
    # Load the dataset (will generate dummy data if CSV is not found)
    header, dataset = load_dataset(DATA_FILENAME)
    
    if header is None:
        return # Stop execution if loading failed

    # Preprocess the dataset
    header, dataset = preprocess_dataset(header, dataset)
    
    if header is None:
        return # Stop execution if preprocessing failed

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(header, dataset)
    
    if X_train is None:
        return # Stop execution if splitting failed
    
    # Print the split datasets (first few entries only for readability)
    print("\n--- Final Split Data (First 3 Samples) ---")
    print(f"Total Features: {len(X_train[0])} including engineered features.")
    print("Training features (X_train[0:3]):", X_train[0:3])
    print("Testing features (X_test[0:3]):", X_test[0:3])
    print("Training labels (y_train[0:3]):", y_train[0:3])
    print("Testing labels (y_test[0:3]):", y_test[0:3])

if __name__ == "__main__":
    main()
