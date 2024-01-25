from models.parking_floor import ParkingFloor

class ParkingLot():

    def __init__(self, parking_lot_name, address, two_wheeler_rate, four_wheeler_rate, eight_wheeler_rate):
        self.name = parking_lot_name
        self.address = address
        self.parking_floors = []
        self.two_wheeler_rate = two_wheeler_rate
        self.four_wheeler_rate = four_wheeler_rate
        self.eight_wheeler_rate = eight_wheeler_rate

    
    def __str__(self):
        parking_floors_str = ",".join(parking_floor.floor_name for parking_floor in self.parking_floors)
        return f"ParkingLot(name={self.name}, address={self.address}, parking_floors={parking_floors_str}, two_wheeler_rate={self.two_wheeler_rate}, four_wheeler_rate={self.four_wheeler_rate}, eight_wheeler_rate={self.eight_wheeler_rate})"

    def add_parking_floor(self, floor_name):
        parking_floor = ParkingFloor(floor_name)
        parking_floor.add_parking_spot("TWO_WHEELER")
        parking_floor.add_parking_spot("TWO_WHEELER")
        parking_floor.add_parking_spot("TWO_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("FOUR_WHEELER")
        parking_floor.add_parking_spot("EIGHT_WHEELER")
        parking_floor.add_parking_spot("EIGHT_WHEELER")
        parking_floor.add_parking_spot("EIGHT_WHEELER")
        parking_floor.add_parking_spot("EIGHT_WHEELER")
        self.parking_floors.append(parking_floor)


    def modify_parking_floor(self, floor_name, spot_type):

        for parking_floor in self.parking_floors:
            if parking_floor.floor_name == floor_name:
                parking_floor.add_parking_spot(spot_type)
                return "ADDED PARKING SPOT."

        return "PARKING FLOOR NOT FOUND!"

    
