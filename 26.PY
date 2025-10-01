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
    try:
        # Drop any rows with missing values
        dataset = [row for row in dataset if all(row)]
        
        # Convert categorical variables to numerical variables
        categorical_cols = [i for i, col in enumerate(header) if not col.isdigit()]
        for row in dataset:
            for col in categorical_cols:
                row[col] = hash(row[col])
        
        return header, dataset
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