from Menu import Pizza, Burger, Drinks, Menu 
from Restaurant import Restaurant
from Users import Chef, Manager, Customer, Server
from Order import Order


def main():
    menu = Menu()

    # add pizza to the menu
    pizza_1 = Pizza('Shutki Pizza', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza("Dal Pizza", 500, 'large', ['dal', 'onion'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beaf', ['goru', 'hati'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 90, True)
    menu.add_menu_item('drinks', coke)
    coffe = Drinks('Mocha', 300, False)
    menu.add_menu_item('drinks', coffe)

    # show menu
    # menu.show_menu()

    restaurant = Restaurant('Sai Baba Restaurant', 2000, menu)

    # add employees
    manager = Manager('Kala Chan', 45454, 'kala@chan.com', 'Kaliakor', 1500, 'Jan 1, 2020', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Rustom Baburci', 454544, '124@gmail.com', 'beradoma', 3500, 'Feb 1, 2020', "Chef", 'Biriyani')
    restaurant.add_employee('chef', chef)

    server = Server('Chotu', 53455, 'cotu.com', 'Kagmara', 500, 'Jan 1, 2020', 'server')
    restaurant.add_employee('server', server)

    # show employees
    # restaurant.show_employees()

    # customer_1 placing an order
    customer_2 = Customer('Shakib Khan', 34343, 'Kingkhan.com', 'banani', 10000)
    order_2 = Order(customer_2, [pizza_3, coffe])
    customer_2.place_order(order_2)
    restaurant.add_order(order_2)

    # customer_1 payig for order_1
    restaurant.recieve_payment(order_2, 2000, customer_2)
    print(f'The revenew is: {restaurant.revenue},and the balance is: {restaurant.balance}. Total expenses till now: {restaurant.expense}')

    # customer_2 placing an order
    customer_2 = Customer('Shahrukh Khan', 34343, 'Kingkhan.com', 'banani', 10000)
    order_2 = Order(customer_2, [pizza_2, burger_1, pizza_1, pizza_3, burger_2, coffe])
    customer_2.place_order(order_2)
    restaurant.add_order(order_2)

    # customer_1 payig for order_1
    restaurant.recieve_payment(order_2, 5000, customer_2)
    print(f'Currently, The revenew is: {restaurant.revenue},and the balance is: {restaurant.balance}. Total expenses till now: {restaurant.expense}')

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print(f'Currently, The revenew is: {restaurant.revenue},and the balance is: {restaurant.balance}. Total expenses till now: {restaurant.expense}')

    restaurant.pay_salary(server)
    print(f'Currently, The revenew is: {restaurant.revenue},and the balance is: {restaurant.balance}. Total expenses till now: {restaurant.expense}')




# call the main
if __name__ == '__main__':
    main()