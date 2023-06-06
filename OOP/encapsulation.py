# encapsulation --> hide details
# access modifier: public, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = 'banani 11' # protected
        self.__balance = initial_deposit # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

rafsun = Bank("Chotto bro", 10000)
rafsun.deposit(40000)

print(rafsun.holder_name)
print(rafsun.get_balance())
print(rafsun._Bank__balance)


# __balance is a Private attribute