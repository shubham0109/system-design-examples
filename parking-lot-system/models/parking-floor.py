from abc import ABC, abstractmethod
from models.parking-spot import TwoWheelerSpot, FourWheelerSpot, EightWheelerSpot

class ParkingFloor():

    count = 0

    def __init__(self, floor_name):
        self.floor_name = floor_name
        self.two_wheeler_parking_spots = []
        self.four_wheeler_parking_spots = []
        self.eight_wheeler_parking_spots = []

    def add_parking_spot(self, spot_type):

        if spot_type == "TWO_WHEELER":
            spot = TwoWheelerSpot(_generate_id())
            self.two_wheeler_parking_spots.append(spot)
            return "TWO_WHEELER PARKING SPOT ADDED."

        elif spot_type == "FOUR_WHEELER":
            spot = FourWheelerSpot(_generate_id())
            self.four_wheeler_parking_spots.append(spot)
            return "FOUR_WHEELER PARKING SPOT ADDED."

        elif spot_type == "EIGHT_WHEELER":
            spot = EightWheelerSpot(_generate_id())
            self.eight_wheeler_parking_spots.append(spot)
            return "EIGHT_WHEELER PARKING SPOT ADDED."

        else:
            return "INVALID PARKING SPOT TYPE!"


    def assign_vehicle_to_parking_spot(self, vehicle, spot_type):

        if spot_type == "TWO_WHEELER":
            for spot in self.two_wheeler_parking_spots:
                if spot.is_occupied() == False:
                    spot.occupy_parking_spot(vehicle)
                    return "Added two wheeler to a parking spot", spot.spot_no

            return "TWO_WHEELER PARKING SPOT NOT FOUND."

        elif spot_type == "FOUR_WHEELER":
            for spot in self.four_wheeler_parking_spots:
                if spot.is_occupied() == False:
                    spot.occupy_parking_spot(vehicle)
                    return "Added four wheeler to a parking spot", spot.spot_no

            return "FOUR_WHEELER PARKING NOT FOUND."

        elif spot_type == "EIGHT_WHEELER":
            for spot in self.eight_wheeler_parking_spots:
                if spot.is_occupied() == False:
                    spot.occupy_parking_spot(vehicle)
                    return "Added eight wheeler to a parking spot", spot.spot_no
           
           return "EIGHT_WHEELER PARKING NOT FOUND."

        else:
            return "INVALID PARKING SPOT TYPE!"


    
    def remove_vehicle_from_parking_spot(self, spot):
        vehicle = spot.vacate_parking_spot()
        return f"Vacated {spot.spot_no} parking spot, {vehicle.get_vehicle_type()} : {vehicle.get_registration_no()}"

    
    def _generate_id(self):
        global count
        count++
        return count
