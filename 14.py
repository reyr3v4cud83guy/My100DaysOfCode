class BankAccount:
    def __init__(self, account_number, account_holder_name, email, phone_number, address, date_of_birth, age, gender, occupation, marital_status, nationality, id_number, id_type, id_issue_date, id_expiration_date, id_issuing_authority, id_issuing_country, id_issuing_state, id_issuing_city, id_issuing_zip_code, id_issuing_address, id_issuing_region):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.marital_status = marital_status
        self.nationality = nationality
        self.id_number = id_number
        self.id_type = id_type
        self.id_issue_date = id_issue_date
        self.id_expiration_date = id_expiration_date
        self.id_issuing_authority = id_issuing_authority
        self.id_issuing_country = id_issuing_country
        self.id_issuing_state = id_issuing_state
        self.id_issuing_city = id_issuing_city
        self.id_issuing_zip_code = id_issuing_zip_code
        self.id_issuing_address = id_issuing_address
        self.id_issuing_region = id_issuing_region
        self.balance = 0
        self.account_history = []
        self.account_status = "Active"
        self.account_type = "Savings"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.account_history.append(f"Deposited ${amount:.2f}, new balance: ${self.balance:.2f}")
            print(f"Deposited ${amount:.2f}, new balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.account_history.append(f"Withdrew ${amount:.2f}, new balance: ${self.balance:.2f}")
            print(f"Withdrew ${amount:.2f}, new balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def display_account_history(self):
        for entry in self.account_history:
            print(entry)

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")
        print(f"Marital Status: {self.marital_status}")
        print(f"Nationality: {self.nationality}")
        print(f"ID Number: {self.id_number}")
        print(f"ID Type: {self.id_type}")
        print(f"ID Issue Date: {self.id_issue_date}")
        print(f"ID Expiration Date: {self.id_expiration_date}")
        print(f"ID Issuing Authority: {self.id_issuing_authority}")
        print(f"ID Issuing Country: {self.id_issuing_country}")
        print(f"ID Issuing State: {self.id_issuing_state}")
        print(f"ID Issuing City: {self.id_issuing_city}")
        print(f"ID Issuing Zip Code: {self.id_issuing_zip_code}")
        print(f"ID Issuing Address: {self.id_issuing_address}")
        print(f"ID Issuing Region: {self.id_issuing_region}")
        print(f"Account Status: {self.account_status}")
        print(f"Account Type: {self.account_type}")

def main():
    account = BankAccount("62862970323787 ", "Abdullahi Osman", "Osman6176@gmail.com", "123-456-7890", "west Road California", "2001-03-01",  22, "Male", "Software Engineer", "Single", "American", "1234567890", "Driver's License", "2020-10-01", "2027-01-01", "DMV", "USA", "California", "Los Angeles", "12345", "123 Main St", "West Coast")
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Account History")
        print("5. Display Account Details")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.display_account_history()
        elif choice == "5":
            account.display_account_details()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()