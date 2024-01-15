from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, vehicle_type, registration_no):
        self.vehicle_type = vehicle_type
        self.registration_no = registration_no

    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod
    def get_registration_no(self):
        pass

class Car(Vehicle):

    def __init__(self, registration_no):
        super().__init__("Car", registration_no)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_registration_no(self):
         return self.registration_no

class Bike(Vehicle):

    def __init__(self, registration_no):
        super().__init__("Bike", registration_no)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_registration_no(self):
         return self.registration_no


class Bus(Vehicle):

    def __init__(self, registration_no):
        super().__init__("Bus", registration_no)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_registration_no(self):
         return self.registration_no


