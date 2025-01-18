class ParkingLot:
    def __init__(self):
        self.parking_spots = []
        self.parking_tickets = []

    def add_parking_spot(self, spot):
        self.parking_spots.append(spot)

    def remove_parking_spot(self, spot):
        if spot in self.parking_spots:
            self.parking_spots.remove(spot)
        else:
            print("Parking spot not found.")

    def park_vehicle(self, vehicle, spot):
        if spot in self.parking_spots:
            self.parking_tickets.append(ParkingTicket(vehicle, spot))
            print(f"Vehicle {vehicle.license_plate} parked in spot {spot.spot_number}.")
        else:
            print("Parking spot not available.")

    def unpark_vehicle(self, vehicle):
        for ticket in self.parking_tickets:
            if ticket.vehicle == vehicle:
                self.parking_tickets.remove(ticket)
                print(f"Vehicle {vehicle.license_plate} unparked.")
                return
        print("Vehicle not found in parking lot.")

    def display_parking_lot(self):
        print("Parking Lot:")
        for spot in self.parking_spots:
            print(f"Spot {spot.spot_number}: {spot.spot_type}")

    def display_parking_tickets(self):
        print("Parking Tickets:")
        for ticket in self.parking_tickets:
            print(f"Vehicle {ticket.vehicle.license_plate} parked in spot {ticket.spot.spot_number}.")

    def display_parking_spots(self):
        print("Parking Spots:")
        for spot in self.parking_spots:
            print(f"Spot {spot.spot_number}: {spot.spot_type}")


class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class ParkingTicket:
    def __init__(self, vehicle, spot):
        self.vehicle = vehicle
        self.spot = spot


class ParkingSpot:
    def __init__(self, spot_number, spot_type):
        self.spot_number = spot_number
        self.spot_type = spot_type


def main():
    parking_lot = ParkingLot()

    while True:
        print("\n1. Add parking spot")
        print("2. Remove parking spot")
        print("3. Park vehicle")
        print("4. Unpark vehicle")
        print("5. Display parking lot")
        print("6. Display parking tickets")
        print("7. Display parking spots")
        print("8. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            spot_number = input("Enter parking spot number: ")
            spot_type = input("Enter parking spot type: ")
            parking_lot.add_parking_spot(ParkingSpot(spot_number, spot_type))
        elif choice == "2":
            spot_number = input("Enter parking spot number: ")
            parking_lot.remove_parking_spot(ParkingSpot(spot_number, ""))
        elif choice == "3":
            license_plate = input("Enter vehicle license plate: ")
            vehicle_type = input("Enter vehicle type: ")
            spot_number = input("Enter parking spot number: ")
            parking_lot.park_vehicle(Vehicle(license_plate, vehicle_type), ParkingSpot(spot_number, ""))
        elif choice == "4":
            license_plate = input("Enter vehicle license plate: ")
            parking_lot.unpark_vehicle(Vehicle(license_plate, ""))
        elif choice == "5":
            parking_lot.display_parking_lot()
        elif choice == "6":
            parking_lot.display_parking_tickets()
        elif choice == "7":
            parking_lot.display_parking_spots()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()