class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, "quantity": quantity}
        self.cart.append(product)

    def checkout(self):
        total = 0

        for item in self.cart:
            total += item['price'] * item['quantity']

        print(total)


swapan = Shopping('Alan Swapon')
swapan.add_to_cart("Watch", 40000, 1)
swapan.add_to_cart('dim', 12, 2)

print(swapan.checkout())
