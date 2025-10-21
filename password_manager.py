import random
import string

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, password):
        self.passwords[website] = password
        print(f"Password for {website} added successfully.")

    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            print(f"Password for {website} deleted successfully.")
        else:
            print("Password not found.")

    def display_passwords(self):
        if not self.passwords:
            print("No passwords stored.")
        else:
            for website, password in self.passwords.items():
                print(f"Website: {website}, Password: {password}")

    def generate_password(self, length, complexity):
        if complexity == "low":
            characters = string.ascii_lowercase
        elif complexity == "medium":
            characters = string.ascii_letters + string.digits
        elif complexity == "high":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid complexity level.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        return password

def main():
    password_manager = PasswordManager()
    while True:
        print("\n1. Add password")
        print("2. Delete password")
        print("3. Display passwords")
        print("4. Generate password")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            website = input("Enter website: ")
            password = input("Enter password: ")
            password_manager.add_password(website, password)
        elif choice == "2":
            website = input("Enter website: ")
            password_manager.delete_password(website)
        elif choice == "3":
            password_manager.display_passwords()
        elif choice == "4":
            length = int(input("Enter password length: "))
            complexity = input("Enter password complexity (low, medium, high): ")
            password = password_manager.generate_password(length, complexity)
            print(f"Generated password: {password}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()