import sys

from models import parking_lot, vehicle, ticket

def create_parking_lot():
    
    parkinglot = parking_lot.ParkingLot(
            parking_lot_name="BLR PARKING LOT",
            address="MG ROAD, BLR",
            two_wheeler_rate=50.00,
            four_wheeler_rate=100.00,
            eight_wheeler_rate=200.00
            )

    parkinglot.add_parking_floor("FLOOR_NO_1")
    parkinglot.add_parking_floor("FLOOR_NO_2")
    return parkinglot


def create_list_of_vehicles():
    
    list_of_vehicles = []

    list_of_vehicles.append(vehicle.Car("Car01"))
    list_of_vehicles.append(vehicle.Car("Car02"))
    list_of_vehicles.append(vehicle.Car("Car03"))
    list_of_vehicles.append(vehicle.Car("Car04"))
    list_of_vehicles.append(vehicle.Car("Car05"))
    list_of_vehicles.append(vehicle.Car("Car06"))
    list_of_vehicles.append(vehicle.Car("Car07"))
    list_of_vehicles.append(vehicle.Car("Car08"))
    list_of_vehicles.append(vehicle.Car("Car09"))
    list_of_vehicles.append(vehicle.Car("Car10"))
    list_of_vehicles.append(vehicle.Car("Car11"))
    list_of_vehicles.append(vehicle.Car("Car12"))
    list_of_vehicles.append(vehicle.Car("Car13"))
    list_of_vehicles.append(vehicle.Car("Car14"))
    list_of_vehicles.append(vehicle.Car("Car15"))
    list_of_vehicles.append(vehicle.Bike("Bike01"))
    list_of_vehicles.append(vehicle.Bike("Bike02"))
    list_of_vehicles.append(vehicle.Bike("Bike03"))
    list_of_vehicles.append(vehicle.Bike("Bike04"))
    list_of_vehicles.append(vehicle.Bike("Bike05"))
    list_of_vehicles.append(vehicle.Bike("Bike06"))
    list_of_vehicles.append(vehicle.Bike("Bike07"))
    list_of_vehicles.append(vehicle.Bike("Bike08"))
    list_of_vehicles.append(vehicle.Bus("Bus01"))
    list_of_vehicles.append(vehicle.Bus("Bus02"))
    list_of_vehicles.append(vehicle.Bus("Bus03"))
    list_of_vehicles.append(vehicle.Bus("Bus04"))
    list_of_vehicles.append(vehicle.Bus("Bus05"))

    return list_of_vehicles


def create_vehicle(vehicle_type: str, reg_no: str):

    if vehicle_type == "Car":
        return vehicle.Car(reg_no)
    elif vehicle_type == "Bike":
        return vehicle.Bike(reg_no)
    else:
        return vehicle.Bus(reg_no)



def park_vehicle(vehicle: vehicle.Vehicle, parkinglot: parking_lot.ParkingLot):

    parking_floors_list = parkinglot.parking_floors
    vehicle_type = ""
    parking_spot = None

    if vehicle.vehicle_type == "Bike":
        vehicle_type = "TWO_WHEELER"
    elif vehicle.vehicle_type == "Car":
        vehicle_type = "FOUR_WHEELER"
    else:
        vehicle_type = "EIGHT_WHEELER"

    for parking_floor in parking_floors_list:
        msg, parking_spot = parking_floor.assign_vehicle_to_parking_spot(vehicle, vehicle_type)

        if parking_spot == None:
            print(msg)
        else:
            print(f"{msg} : {parking_spot.spot_no}")
            break
    

    return parking_spot


def generate_ticket(parking_spot):
    
    generated_ticket = ticket.Ticket(parking_spot)
    return generated_ticket



def unpark_vehicle(parking_ticket: ticket.Ticket):
    parking_spot = parking_ticket.parking_spot
    vehicle = parking_spot.vacate_parking_spot()
    parking_ticket.make_payment(amount=100.0)
    return parking_ticket


if __name__ == "__main__":
    parkinglot = create_parking_lot()
    #list_of_vehicles = create_list_of_vehicles()

    print(parkinglot)
    
    #for vehicle in list_of_vehicles:
    #    print(vehicle)

    flag = True
    saved_ticket = None
    while (flag == True):

        print("--------------------------------")
        print("---------MY PARKING LOT---------")
        print("--------------------------------")
        

        print("Enter 1 for vehicle entry")
        print("Enter 2 for vehicle exit")
        print("Enter 3 to exit the menu")

        choice = int(input("Enter your choice: "))
        

        match choice:
            case 1:
                vehicle_type = input("Enter type of vehicle(Car, Bike, Bus): ")
                registration_no = input("Enter the registration number: ")
                
                # Create a vehicle object
                vehicle = create_vehicle(vehicle_type, registration_no)

                # Assign a spot
                parking_spot = park_vehicle(vehicle, parkinglot)

                if parking_spot == None:
                    print("Sorry, No spot available!!!")
                else:
                    print("Your car is parked at {parking_spot.spot_no}")
                    ticket = generate_ticket(parking_spot)
                    saved_ticket = ticket
                    print("Your ticket is being generated...")
                    print("Ticket")
                    print(ticket)

            case 2:
                ticket_no = input("Enter ticket number: ")

                # Get the ticket from DB using ticket_no.  In here we are going to use saved_ticket
                returned_ticket = unpark_vehicle(saved_ticket)

                print("Your ticket is being processed...")
                print("Ticket")
                print(ticket)

                # Can generate invoice

            case 3:
                print("BYE BYE!!!")
                flag = False



