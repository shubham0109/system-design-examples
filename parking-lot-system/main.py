from models.parking-lot import ParkingLot

def create_parking_lot():
    
    parking_lot = ParkingLot(
            name="BLR PARKING LOT",
            address="MG ROAD, BLR",
            two_wheeler_rate=50.00,
            four_wheeler_rate=100.00,
            eight_wheeler_rate=200.00
            )

    parking_lot.add_parking_floor("FLOOR_NO_1")
    parking_lot.add_parking_floor("FLOOR_NO_2")

if __name__ == "__main__":
    create_parking_lot()
