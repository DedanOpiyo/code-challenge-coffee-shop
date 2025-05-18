# Import the necessary classes
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

# Create two customers
c1 = Customer("Jane")
c2 = Customer("Elli")

# Create two coffee types
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
