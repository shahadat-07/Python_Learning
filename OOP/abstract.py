from abc import ABC, abstractmethod # here abc means abstract base class

class Animal(ABC):
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        print("I need food")

    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = "Monkey"
        super().__init__()

    def eat(self):
        print("I am eating banana")


Lucky = Monkey("Lucky")
Lucky.eat()