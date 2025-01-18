class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.income = 0

    def add_expense(self, name, amount):
        if amount < 0:
            print("Expense amount cannot be negative.")
        else:
            self.expenses[name] = amount

    def remove_expense(self, name):
        if name in self.expenses:
            del self.expenses[name]
        else:
            print("Expense not found.")

    def display_expenses(self):
        if not self.expenses:
            print("No expenses added.")
        else:
            for name, amount in self.expenses.items():
                print(f"{name}: ${amount:.2f}")

    def add_income(self, amount):
        if amount < 0:
            print("Income amount cannot be negative.")
        else:
            self.income += amount

    def display_income(self):
        print(f"Total income: ${self.income:.2f}")

    def calculate_total_expenses(self):
        return sum(self.expenses.values())

    def display_balance(self):
        total_expenses = self.calculate_total_expenses()
        balance = self.income - total_expenses
        print(f"Total expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add expense")
        print("2. Remove expense")
        print("3. Display expenses")
        print("4. Add income")
        print("5. Display income")
        print("6. Display balance")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.add_expense(input("Enter expense name: "), float(input("Enter expense amount: ")))
        elif choice == "2":
            tracker.remove_expense(input("Enter expense name: "))
        elif choice == "3":
            tracker.display_expenses()
        elif choice == "4":
            tracker.add_income(float(input("Enter income amount: ")))
        elif choice == "5":
            tracker.display_income()
        elif choice == "6":
            tracker.display_balance()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()