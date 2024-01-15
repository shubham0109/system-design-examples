from abc import ABC, abstractmethod
from models.vehicle import Vehicle 

class ParkingSpot(ABC):

    def __init__(self, spot_no, spot_type, is_occupied=False):
        self.spot_no = spot_no
        self.spot_type = spot_type
        self.is_occupied = is_occupied
        self.vehicle = None

    @abstractmethod
    def is_occupied(self):
        pass

    @abstractmethod
    def occupy_parking_spot(self, vehicle):
        pass

    @abstractmethod
    def vacate_parking_spot(self):
        pass

class TwoWheelerSpot(ParkingSpot):
    
    def __init__(self, spot_no):
        super().__init__(spot_no, "TWO_WHEELER")

    def is_occupied(self):
        return self.is_occupied

    def occupy_parking_spot(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def vacate_parking_spot(self):
        vehicle = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return vehicle

class FourWheelerSpot(ParkingSpot):

    def __init__(self, spot_no):
        super().__init__(spot_no, "FOUR_WHEELER")

    def is_occupied(self):
        return self.is_occupied

    def occupy_parking_spot(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def vacate_parking_spot(self):
        vehicle = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return vehicle

class EightWheelerSpot(ParkingSpot):

    def __init__(self, spot_no):
        super().__init__(spot_no, "EIGHT_WHEELER")

    def is_occupied(self):
        return self.is_occupied

    def occupy_parking_spot(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def vacate_parking_spot(self):
        vehicle = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return vehicle

