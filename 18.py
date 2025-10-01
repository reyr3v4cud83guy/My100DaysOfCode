 my_branch
from datetime import datetime

class WaterMeter:
    def __init__(self):
        self.total_water_used = 0
        self.water_used_monthly = {}
        self.current_date = datetime.now()
        self.fees_per_unit = 0.5

    def add_water_used(self, amount):
        self.total_water_used += amount
        current_month = self.current_date.strftime("%B")
        if current_month in self.water_used_monthly:
            self.water_used_monthly[current_month] += amount
        else:
            self.water_used_monthly[current_month] = amount

    def display_info(self):
        print(f"Current Date and Time: {self.current_date}")
        print(f"Total Water Used: {self.total_water_used} units")

    def display_monthly_water_used(self):
        for month, amount in self.water_used_monthly.items():
            print(f"{month}: {amount} units")

    def calculate_monthly_fees(self):
        for month, amount in self.water_used_monthly.items():
            fees = amount * self.fees_per_unit
            print(f"{month} fees: ${fees:.2f}")

    def main(self):
        while True:
            print("1. Add Water Used")
            print("2. Display Info")
            print("3. Display Monthly Water Used")
            print("4. Calculate Monthly Fees")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_water_used(float(input("Enter the amount of water used: ")))
            elif choice == "2":
                self.display_info()
            elif choice == "3":
                self.display_monthly_water_used()
            elif choice == "4":
                self.calculate_monthly_fees()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    water_meter = WaterMeter()
=======
  my_branch
from datetime import datetime

class WaterMeter:
    def __init__(self):
        self.total_water_used = 0
        self.water_used_monthly = {}
        self.current_date = datetime.now()
        self.fees_per_unit = 0.5

    def add_water_used(self, amount):
        self.total_water_used += amount
        current_month = self.current_date.strftime("%B")
        if current_month in self.water_used_monthly:
            self.water_used_monthly[current_month] += amount
        else:
            self.water_used_monthly[current_month] = amount

    def display_info(self):
        print(f"Current Date and Time: {self.current_date}")
        print(f"Total Water Used: {self.total_water_used} units")

    def display_monthly_water_used(self):
        for month, amount in self.water_used_monthly.items():
            print(f"{month}: {amount} units")

    def calculate_monthly_fees(self):
        for month, amount in self.water_used_monthly.items():
            fees = amount * self.fees_per_unit
            print(f"{month} fees: ${fees:.2f}")

    def main(self):
        while True:
            print("1. Add Water Used")
            print("2. Display Info")
            print("3. Display Monthly Water Used")
            print("4. Calculate Monthly Fees")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_water_used(float(input("Enter the amount of water used: ")))
            elif choice == "2":
                self.display_info()
            elif choice == "3":
                self.display_monthly_water_used()
            elif choice == "4":
                self.calculate_monthly_fees()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    water_meter = WaterMeter()
=======
from datetime import datetime

class WaterMeter:
    def __init__(self):
        self.total_water_used = 0
        self.water_used_monthly = {}
        self.current_date = datetime.now()
        self.fees_per_unit = 0.5

    def add_water_used(self, amount):
        self.total_water_used += amount
        current_month = self.current_date.strftime("%B")
        if current_month in self.water_used_monthly:
            self.water_used_monthly[current_month] += amount
        else:
            self.water_used_monthly[current_month] = amount

    def display_info(self):
        print(f"Current Date and Time: {self.current_date}")
        print(f"Total Water Used: {self.total_water_used} units")

    def display_monthly_water_used(self):
        for month, amount in self.water_used_monthly.items():
            print(f"{month}: {amount} units")

    def calculate_monthly_fees(self):
        for month, amount in self.water_used_monthly.items():
            fees = amount * self.fees_per_unit
            print(f"{month} fees: ${fees:.2f}")

    def main(self):
        while True:
            print("1. Add Water Used")
            print("2. Display Info")
            print("3. Display Monthly Water Used")
            print("4. Calculate Monthly Fees")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_water_used(float(input("Enter the amount of water used: ")))
            elif choice == "2":
                self.display_info()
            elif choice == "3":
                self.display_monthly_water_used()
            elif choice == "4":
                self.calculate_monthly_fees()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    water_meter = WaterMeter()
 Osman--branch
    water_meter.main()