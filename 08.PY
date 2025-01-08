import re

def verify_email(email):
    """
    Verifies if the given email address is valid.
    
    Args:
        email (str): The email address to verify.
    
    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def main():
    # Test the verify_email function
    emails = ["test@example.com", "test.example.com", "test@.com"]
    for email in emails:
        print(f"Email: {email}, Valid: {verify_email(email)}")

if __name__ == "__main__":
    main()