import psutil

class TemperatureSensor:
    def __init__(self):
        self.temperature = psutil.sensors_temperatures()

    def get_temperature(self):
        if self.temperature:
            return self.temperature['coretemp'][0].current
        else:
            return None

    def convert_to_fahrenheit(self, temperature):
        return (temperature * 9/5) + 32

    def convert_to_celsius(self, temperature):
        return (temperature - 32) * 5/9

    def display_temperature(self):
        temperature = self.get_temperature()
        if temperature:
            print(f"Temperature in Celsius: {temperature}°C")
            print(f"Temperature in Fahrenheit: {self.convert_to_fahrenheit(temperature)}°F")
        else:
            print("Unable to retrieve temperature.")

def main():
    sensor = TemperatureSensor()
    while True:
        print("\n1. Display temperature")
        print("2. Convert temperature to Fahrenheit")
        print("3. Convert temperature to Celsius")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sensor.display_temperature()
        elif choice == "2":
            temperature = float(input("Enter temperature in Celsius: "))
            print(f"{temperature}°C is equal to {sensor.convert_to_fahrenheit(temperature)}°F")
        elif choice == "3":
            temperature = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temperature}°F is equal to {sensor.convert_to_celsius(temperature)}°C")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

 