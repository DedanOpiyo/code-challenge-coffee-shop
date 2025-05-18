# # customer.py
# from coffee import Coffee
# from order import Order

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
        # from order import Order
        return [order for order in Order.orders if order.customer == self]
    
    def coffees(self):
        # unique list of `Coffee` instances. 
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price): # validations will be done by Order class
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

# # Test
# customer = Customer("James")
# print(customer.name)


# # coffee.py
# from order import Order
# # from lib.order import Order

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
        # from order import Order
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

# # order.py
# from customer import Customer
# from coffee import Coffee

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



# Test
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
print(coffee.customers()[0].name)
# => James
print(coffee.num_orders())
# => 2
print(coffee.average_price())
# => 2.0


# Customer class' methods
print(customer.orders())
# => [<__main__.Order object at 0x7f0404a02f30>]
print(customer.coffees()[0].name)
# => Espresso
print(customer.create_order(coffee2, 4.0)) # a second order for the same customer instance => from Customer class.
print((customer.most_aficionado(coffee)).name)
# => Jane 

