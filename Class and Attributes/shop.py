class Shop:
    cart = []  # Here cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehzabeen = Shop("meh jabeen")
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart("phone")
print(mehzabeen.cart)

nisho = Shop("noisho")
nisho.add_to_cart("Cap")
nisho.add_to_cart("Watch")
print(nisho.cart)
