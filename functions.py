def greet(name: str) -> None:
    """Prints a personalized greeting message"""
    print(f"Hello, {name.title()}!")

def add(x: int, y: int) -> int:
    """Returns the sum of two numbers"""
    return x + y

def subtract(x: int, y: int) -> int:
    """Returns the difference of two numbers"""
    return x - y

def multiply(x: int, y: int) -> int:
    """Returns the product of two numbers"""
    return x * y

def divide(x: int, y: int) -> float:
    """Returns the quotient of two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main() -> None:
    """Main function to test the greet and math functions"""
    greet("Abdullahi")
    print(add(5, 10))
    print(subtract(10, 5))
    print(multiply(5, 10))
    try:
        print(divide(10, 2))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()