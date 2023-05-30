class Car:
    # name = ""
    # color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Starting the engine")
        print("The name of the car is:", self.name)
        print("Color:", self.color)


my_car1 = Car("Corolla", "White")
my_car1.start()
my_car2 = Car("Asios", "Black")
my_car2.start()
