class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'Name: {self.name}, Price: {self.price}'

    def move (self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight) #Here  happened the multi-level inheritance

class ACBus(Bus):
    def __init__(self, name, price, seat, temparature) -> None:
        self.temparature= temparature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f' Seat: {self.seat}, Temparature: {self.temparature}')
        return super().__repr__()

green_line = ACBus('green', 5000000, 22, 16)
print(green_line)