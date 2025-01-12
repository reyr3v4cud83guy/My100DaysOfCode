class PowerUsageTracker:
    def __init__(self):
        self.devices = {}
        self.cost_per_unit = 0

    def add_device(self, name, power_usage):
        if power_usage < 0:
            print("Power usage cannot be negative.")
        else:
            self.devices[name] = power_usage

    def remove_device(self, name):
        if name in self.devices:
            del self.devices[name]
        else:
            print("Device not found.")

    def display_devices(self):
        if not self.devices:
            print("No devices added.")
        else:
            for name, power_usage in self.devices.items():
                print(f"{name}: {power_usage} units")

    def calculate_total_power_usage(self):
        return sum(self.devices.values())

    def display_total_power_usage(self):
        total_power_usage = self.calculate_total_power_usage()
        print(f"Total power usage: {total_power_usage} units")

    def set_cost_per_unit(self, cost):
        if cost < 0:
            print("Cost per unit cannot be negative.")
        else:
            self.cost_per_unit = cost

    def calculate_total_cost(self):
        total_power_usage = self.calculate_total_power_usage()
        return total_power_usage * self.cost_per_unit

    def display_total_cost(self):
        total_cost = self.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")

    def display_device_cost(self):
        if not self.devices:
            print("No devices added.")
        else:
            for name, power_usage in self.devices.items():
                device_cost = power_usage * self.cost_per_unit
                print(f"{name}: ${device_cost:.2f}")

def main():
    tracker = PowerUsageTracker()
    while True:
        print("\n1. Add device")
        print("2. Remove device")
        print("3. Display devices")
        print("4. Calculate total power usage")
        print("5. Set cost per unit")
        print("6. Calculate total cost")
        print("7. Display device cost")
        print("8. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.add_device(input("Enter device name: "), float(input("Enter power usage: ")))
        elif choice == "2":
            tracker.remove_device(input("Enter device name: "))
        elif choice == "3":
            tracker.display_devices()
        elif choice == "4":
            tracker.display_total_power_usage()
        elif choice == "5":
            tracker.set_cost_per_unit(float(input("Enter cost per unit: ")))
        elif choice == "6":
            tracker.display_total_cost()
        elif choice == "7":
            tracker.display_device_cost()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()