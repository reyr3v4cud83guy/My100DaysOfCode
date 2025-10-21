import datetime

class CalorieTracker:
    def __init__(self):
        self.calories_consumed = 0
        self.calories_burned = 0
        self.net_calories = 0

    def add_food(self, calories):
        self.calories_consumed += calories
        self.calculate_net_calories()

    def add_exercise(self, calories):
        self.calories_burned += calories
        self.calculate_net_calories()

    def calculate_net_calories(self):
        self.net_calories = self.calories_consumed - self.calories_burned

    def display_calories(self):
        print(f"Calories Consumed: {self.calories_consumed}")
        print(f"Calories Burned: {self.calories_burned}")
        print(f"Net Calories: {self.net_calories}")

    def save_data(self):
        with open("calorie_data.txt", "a") as file:
            file.write(f"{datetime.datetime.now()}: Calories Consumed={self.calories_consumed}, Calories Burned={self.calories_burned}, Net Calories={self.net_calories}\n")

    def load_data(self):
        try:
            with open("calorie_data.txt", "r") as file:
                for line in file.readlines():
                    print(line.strip())
        except FileNotFoundError:
            print("No data found.")

def main():
    tracker = CalorieTracker()
    while True:
        print("\n1. Add Food")
        print("2. Add Exercise")
        print("3. Display Calories")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            calories = float(input("Enter calories consumed: "))
            tracker.add_food(calories)
        elif choice == "2":
            calories = float(input("Enter calories burned: "))
            tracker.add_exercise(calories)
        elif choice == "3":
            tracker.display_calories()
        elif choice == "4":
            tracker.save_data()
        elif choice == "5":
            tracker.load_data()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()