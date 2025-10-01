import csv
import warnings
warnings.filterwarnings("ignore")

# Define a function to load the dataset
def load_dataset(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        header = data[0]
        dataset = data[1:]
        return header, dataset
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to preprocess the dataset
def preprocess_dataset(header, dataset):
    import random
    import math
    try:
        if not header or not dataset:
            print("Header or dataset is missing.")
            return header, dataset
        # Drop any rows with missing values
        dataset = [row for row in dataset if all(row)]

        # Remove outliers (for numeric columns, values outside 0-100)
        def is_outlier(row):
            for i in range(len(row)):
                try:
                    val = float(row[i])
                    if val < 0 or val > 100:
                        return True
                except ValueError:
                    continue
            return False
        dataset = [row for row in dataset if not is_outlier(row)]

        # Shuffle dataset
        random.shuffle(dataset)

        # Detect categorical columns by checking if all values in a column are non-numeric
        categorical_cols = []
        numeric_cols = []
        for i in range(len(header)):
            is_categorical = False
            for row in dataset:
                try:
                    float(row[i])
                except ValueError:
                    is_categorical = True
                    break
            if is_categorical:
                categorical_cols.append(i)
            else:
                numeric_cols.append(i)

        # One-hot encode categorical columns
        # (for demonstration, but your sample data is all numeric)
        # If you add categorical data, this will work
        unique_values = {col: list(set(row[col] for row in dataset)) for col in categorical_cols}
        new_header = []
        for i, col_name in enumerate(header):
            if i in categorical_cols:
                for val in unique_values[i]:
                    new_header.append(f"{col_name}_{val}")
            else:
                new_header.append(col_name)
        new_dataset = []
        for row in dataset:
            new_row = []
            for i in range(len(row)):
                if i in categorical_cols:
                    for val in unique_values[i]:
                        new_row.append(1 if row[i] == val else 0)
                else:
                    new_row.append(float(row[i]))
            new_dataset.append(new_row)

        # Feature engineering: add sum and average of lottery numbers as new features
        # Assume lottery numbers are numeric columns except 'target'
        target_index = header.index('target') if 'target' in header else -1
        sum_idx = len(new_header)
        avg_idx = len(new_header) + 1
        new_header += ['numbers_sum', 'numbers_avg']
        for row in new_dataset:
            nums = [row[i] for i in numeric_cols if i != target_index]
            row.append(sum(nums))
            row.append(sum(nums)/len(nums) if nums else 0)

        # Normalization (min-max scaling for numeric columns)
        # Find min and max for each numeric column
        min_vals = [min(row[i] for row in new_dataset) for i in range(len(new_header))]
        max_vals = [max(row[i] for row in new_dataset) for i in range(len(new_header))]
        for row in new_dataset:
            for i in range(len(new_header)):
                if max_vals[i] != min_vals[i]:
                    row[i] = (row[i] - min_vals[i]) / (max_vals[i] - min_vals[i])
                else:
                    row[i] = 0.0

        return new_header, new_dataset
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to split the dataset into training and testing sets
def split_dataset(header, dataset, test_size=0.2):
    try:
        # Split the dataset into features (X) and target variable (y)
        target_index = header.index('target')
        X = [row[:target_index] + row[target_index+1:] for row in dataset]
        y = [row[target_index] for row in dataset]
        
        # Convert features and target to float
        X = [[float(value) for value in row] for row in X]
        y = [float(value) for value in y]
        
        # Split the dataset into training and testing sets
        split_index = int(len(X) * (1 - test_size))
        X_train, X_test = X[:split_index], X[split_index:]
        y_train, y_test = y[:split_index], y[split_index:]
        
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Load the dataset
    header, dataset = load_dataset('lottery_data.csv')
    
    # Preprocess the dataset
    header, dataset = preprocess_dataset(header, dataset)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(header, dataset)
    
    # Print the split datasets
    print("Training features:", X_train)
    print("Testing features:", X_test)
    print("Training labels:", y_train)
    print("Testing labels:", y_test)

if __name__ == "__main__":
    main()