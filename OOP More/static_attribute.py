# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method adn class method

class Shopping:
    cart = []  # class attribute --> static attribute
    origin = 'china'
    def __init__(self, name, location) -> None:
        self.name = name #instance attribute
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply( a, b):
        result = a*b
        print(result)

    @classmethod
    def huday_dekhi(self, item):
        print("Huday", item)

basundhara = Shopping('basu', 'dhara')
# basundhara.purchase('kola', 500, 1000)
basundhara.huday_dekhi('lungi')
# Shopping.purchase('a', 2, 3, 4)

Shopping.multiply(4, 4)


