class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        print('vat mangos polau korma')

    def exercise(self):
        raise NotADirectoryError

class Crickter(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # over ride
    def eat(self):
        print("Vegetables")

    def exercise(self):
        print("Doing exercise")
        
    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.age * other.age

shakib = Crickter('sakib', 38, 68, 91, 'BD')
mushi  = Crickter('mushi', 35, 65, 89, 'BD')
# shakib.eat()
# shakib.exercise()


# Plus sign overload
print(45 + 63)
print('Shakib' + " " + "Al" +  " " + "Hasan")
print([1, 2] + [3, 4])
print(shakib + mushi)
print(shakib * mushi)