# coffee.py
# from order import Order
# from lib.order import Order

class Coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name of coffee must be a string")
        if not 3 <= len(name):
            raise ValueError("Name of coffee should be at least 3 characters long")
        self._name = name

    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if self.orders():
            return sum(order.price for order in self.orders()) / self.num_orders()
        return "No orders have been made yet"


# # Test
# coffee = Coffee("Espresso")
# print(coffee.name)
# print(coffee.orders())