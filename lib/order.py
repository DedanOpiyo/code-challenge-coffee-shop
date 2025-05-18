# order.py
from customer import Customer
from coffee import Coffee

class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.orders.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer class")
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee class")
        self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a float/number")
        if not 1.0 <= float(value) <= 10.0:
            raise ValueError("Price should fall between 1.0 and 10.0")
        self._price = float(value)



# # Test
customer = Customer("James")
print(customer.name)
# => James

customer2 = Customer("Jane") # another Customer instance to test most_aficionado()

coffee = Coffee("Espresso")
coffee2 = Coffee("Americano")
print(coffee.name)
# => Espresso

order = Order(customer, coffee, 2.0)
order2 = Order(customer2, coffee, 2.0) # order from another customer-customer2. We order the same coffee, but customer will order twice, from create_order method in Custoner class
print(order.price)
# => 2.0
print(order.coffee)
# => <__main__.Coffee object at 0x7f0404a01eb0>  -customer object
print(order.orders[0].coffee.name)
# => Espresso


# Coffee class' methods
print(coffee.orders())
# => [<__main__.Order object at 0x7f0404a02f30>, <__main__.Order object at 0x7f0404a02fc0>]
print(coffee.customers())
# print(coffee.customers()[0].name)
# => James
print(coffee.num_orders())
# => 2
print(coffee.average_price())
# => 2.0


# Customer class' methods
print(customer.orders())
# => [<__main__.Order object at 0x7f0404a02f30>]
print(customer.coffees())
# print(customer.coffees()[0].name)
# => Espresso
print(customer.create_order(coffee2, 4.0)) # a second order for the same customer instance => from Customer class.
print((customer.most_aficionado(coffee)))
# => Jane