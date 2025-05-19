# # Import the classes
# from lib.customer import Customer
# from lib.coffee import Coffee
# from lib.order import Order

# Modifying sys.path, directing Python where to look
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from customer import Customer
from coffee import Coffee
from order import Order


# Creating two customers
c1 = Customer("Jane")
c2 = Customer("Elli")

# Creating two coffee types
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Jane creates two orders
o1 = c1.create_order(latte, 4.5)
o2 = c1.create_order(espresso, 3.0)

# Elli creates two orders (both for Latte)
o3 = c2.create_order(latte, 5.0)
o4 = c2.create_order(latte, 5.5)

# Print all coffee types that Jane has ordered
print("Jane's coffees:", [coffee.name for coffee in c1.coffees()])  # ['Latte', 'Espresso']

# Print all customers who have ordered Latte
print("Customers who ordered Latte:", [customer.name for customer in latte.customers()])  # ['Jane', 'Elli']

# Print number of times Latte was ordered
print("Number of orders for Latte:", latte.num_orders())  # 3

# Print average price for Latte
print("Average price for Latte:", latte.average_price())  # (4.5 + 5.0 + 5.5) / 3

# Find the customer who spent the most on Latte
aficionado = Customer.most_aficionado(latte)
if aficionado:
    print("Most aficionado for Latte:", aficionado.name)  # Likely "Elli"
else:
    print("No aficionado found.")

## Other Logical Tests

print("---------------- Customer names & Coffee names:\n")
# Other Logs- Testing direct order creation, and Coffee and Customer methods, Logically
print(f"c1: {c1.name}") # => Jane
print(f"c2: {c2.name}") # => Elli
print(f"Instance of latte coffee: {latte.name}") # => Latte
print(f"Instance of espresso coffee: {espresso.name}") # => Espresso

print("---------------- Creating direct orders:\n")
# Creating direct orders
o5 = Order(c1, espresso, 2.0)
o6 = Order(c2, latte, 2.0) 
print(f"The 5th order was completed for C1, who ordered an Espresso at: {o5.price}") # => 2.0
print(f"Coffee object from the fifth order: {o5.coffee}") # => <__main__.Coffee object at 0x7f0404a01eb0>  # customer object
print(f"First coffee order — coffee name: {o5.orders[0].coffee.name}") # => Latte

print("---------------- Coffee class methods:\n")
# Coffee class' methods
print(latte.orders()) # => [<order.Order object at 0x7f182da43620>, <order.Order object at 0x7f182da43650>, <order.Order object at 0x7f182da43680>, <order.Order object at 0x7f182da436e0>]
print(latte.customers()[0].name) # => Elli
print(latte.num_orders()) # => 4
print(latte.average_price()) # => 4.5

print("---------------- Customer Class methods:\n")
# Customer class' methods
print(c1.orders()) # => [<order.Order object at 0x7fc0d6d33aa0>, <order.Order object at 0x7fc0d6d33ad0>, <order.Order object at 0x7fc0d6d33b60>]
print(c1.coffees()[0].name) # => Latte
print(c1.create_order(espresso, 4.0)) # => <order.Order object at 0x7fc0d6d33bf0> # another order from c1. She now has 4 orders.
print((c1.most_aficionado(espresso)).name) # => Jane 

