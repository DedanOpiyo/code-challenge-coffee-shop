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