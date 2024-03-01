def get_room_cost(room_type, duration, num_rooms):
    # Define room types and their nightly rates
    room_types = {"1": 100, "2": 150, "3": 250}

    # Calculate the total cost based on the selected room type, duration, and number of rooms
    if room_type in room_types:
        return room_types[room_type] * duration * num_rooms
    else:
        return None


def calculate_services_cost(services):
    # Define additional services and their rates
    service_rates = {"1": 20, "2": 10, "3": 15}
    total_cost = 0

    # Calculate the total cost of selected additional services
    for service in services:
        if service in service_rates:
            total_cost += service_rates[service]

    return total_cost


def main():
    print()
    print("Welcome to the Transylvania Hotel Reservation System!")
    print()
    print("1. Single Room = RM100 per night")
    print("2. Double Room = RM150 per night")
    print("3. Suite = RM250 per night")
    print()

    # User input for room type, number of rooms, duration of stay, and additional services
    name = input("Please Enter Name: ")
    room_type = input("Enter room type (1 / 2 / 3): ")
    num_rooms = int(input("Enter number of rooms: "))
    duration = int(input("Enter duration of stay (in nights): "))
    date_in = input("Enter Your Check In Date (YYYY-MM-DD) : ")
    date_out = input("Enter your Check Out Date (YYYY-MM-DD) : ")
    print()
    additional_services = input("Would you like to add any additional services? (yes/no): ")
    if additional_services.lower() == "yes":
        print()
        print("Additional Service :")
        print()
        print("1. Breakfast - RM20 per person")
        print("2. Wifi - RM10 per day")
        print("3. Parking - RM15 per day")
        print()
        additional_services = input(
            "Enter additional services separated by commas (e.g., 1 / 2 / 3): ").split(",")
    else:
        additional_services = []

    # Calculate the total cost of the room
    room_cost = get_room_cost(room_type, duration, num_rooms)
    if room_cost is None:
        print("Invalid room type.")
        return

    # Calculate the total cost of additional services
    additional_services_cost = calculate_services_cost([service.strip() for service in additional_services])

    # Calculate total cost from room cost and additional service cost
    total_cost = room_cost + additional_services_cost

    # Show the details of the reservation
    print()
    print(f"Name: {name}")
    print("\nReservation Details:")
    print(f"Room Type: {room_type}")
    print(f"Number of Rooms: {num_rooms}")
    print(f"Duration of Stay: {duration} nights")
    print(f"Check In Date: {date_in}")
    print(f"Check Out Date: {date_out}")


    print("\nAdditional Services:")
    for service in additional_services:
        if service == "1":
            print(" Breakfast = RM20 per person")
        elif service == "2":
            print(" Wifi = RM10 per day")
        elif service == "3":
            print(" Parking = RM15 per day")

    print()
    print(f"Total Cost: RM {total_cost:.2f}")

if __name__ == "__main__":
    main()


