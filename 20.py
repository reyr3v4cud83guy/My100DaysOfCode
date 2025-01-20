import subprocess
import os

def compile_and_run(file_path):
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError

        # Check if the file is a Python file
        if not file_path.endswith('.py'):
            raise ValueError("Only Python files are supported")

        # Compile the Python code
        compile_command = f"python -m py_compile {file_path}"
        subprocess.check_call(compile_command, shell=True)

        # Get the compiled file path
        compiled_file_path = file_path + 'c'

        # Run the compiled Python code
        run_command = f"python {compiled_file_path}"
        subprocess.check_call(run_command, shell=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")

    except PermissionError:
        print("Permission denied. Please check the file permissions.")

    except ValueError as e:
        print(f"Invalid input: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        file_path = input("Enter the file path (or 'q' to quit): ")
        if file_path.lower() == 'q':
            break
        compile_and_run(file_path)

if __name__ == "__main__":
    main()