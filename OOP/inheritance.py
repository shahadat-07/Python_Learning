#base class, parent class, common attribute + functionality class
#derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
         self.brand = brand
         self.price = price
         self.color = color
         self.origin = origin

    def run(self):
        return f'running laptop: {self.brand}'

class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'learing python and practicing'
    

class Phone(Gadget):
    def __init__(self, brand, price, origin, color, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, origin, color)

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with {text}'
    
    def __repr__(self) -> str:
        return f'Phone: IsDualSim: {self.dual_sim} {self.brand} {self.price} {self.origin}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_les(self):
        pass



#inheritance
my_phone = Phone('Iphone', 120000, 'silver', 'china', True)
# my_phone.phone_call()

print(my_phone.brand)

print(my_phone)
