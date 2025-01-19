from datetime import datetime
from datetime import timedelta

class WaterMeter:
    def __init__(self):
        self.total_water_used = 0
        self.water_used_today = 0
        self.water_used_yesterday = 0
        self.current_date = datetime.now()

    def add_water_used(self, amount):
        self.total_water_used += amount
        self.water_used_today += amount

    def display_info(self):
        print(f"Current Date and Time: {self.current_date}")
        print(f"Total Water Used: {self.total_water_used} units")
        print(f"Water Used Today: {self.water_used_today} units")

    def display_yesterday_water_used(self):
        print(f"Water Used Yesterday: {self.water_used_yesterday} units")

    def calculate_yesterday_water_used(self):
        today = datetime.now()
        if today.date() != self.current_date.date():
            self.water_used_yesterday = self.water_used_today
            self.water_used_today = 0
            self.current_date = today

    def main(self):
        while True:
            print("1. Add Water Used")
            print("2. Display Info")
            print("3. Display Yesterday's Water Used")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_water_used(float(input("Enter the amount of water used: ")))
            elif choice == "2":
                self.display_info()
            elif choice == "3":
                self.calculate_yesterday_water_used()
                self.display_yesterday_water_used()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    water_meter = WaterMeter()
    water_meter.main()