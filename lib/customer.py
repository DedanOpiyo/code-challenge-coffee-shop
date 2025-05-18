# customer.py

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name of the customer must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name of the customer should be between 1 to 15 characters long")
        self._name = name

    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.customer == self]
    
    def coffees(self):
        # unique list of `Coffee` instances. 
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price): # validations will be done by Order class
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        all_customers = coffee.customers() # unique list of customers
        
        current_max_spent = 0
        highest_spender = None
        
        for customer in all_customers:
            total_spent = 0

            for order in coffee.orders():
                if customer == order.customer: # for orders specific to this customer
                   total_spent += order.price

            if total_spent > current_max_spent:
                current_max_spent = total_spent
                highest_spender = customer
            
        return highest_spender