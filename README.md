# Coffee Shop Domain Modeling
## Objective
The objective is to create a Python application from scratch to model a Coffee Shop domain. Object-oriented programming principles should guide the implementations. The project showcases the ability to design classes, implement methods, establish relationships between objects, and handle data appropriately.

## Implementations

1. Setup and Preparation
### prerequisite 

   - Create a new directory for your project named `coffee_shop`.
   - Set up a virtual environment within this directory using `pipenv`:
     ```bash
     pipenv install
     pipenv shell
     ```
   - Install any necessary packages, such as `pytest` for testing:
     ```bash
     pipen

-**Refer to step three for file creation if you want to create the project from scratch: 3. Create Class Files
-**Alternatively fork and clone the repo to follow along with the code and run:
```bash
pipenv install
pipenv shell
```


2. Domain Model Design
### prerequisite 

 - Before coding, sketch your domain model on paper or a whiteboard:
 - Identify the three main classes: `Customer`, `Coffee`, and `Order`.
 - Establish the relationships between these classes.
   - Determine the attributes and methods that each class will have.
   - Keep in mind the concept of a single source of truth for your data.

### implementation

**Pseudocode**
*-Coffee shop domain model constitute:
Customers, coffee, and an order.
A customer interacts with the shop by making an order.
A customer orders coffee.
A customer can order more than one coffee.
Coffee is ordered by the customer.
For coffee to be ordered, it needs a customer.
We need to keep track of who orders our coffee.
We need to keep track of the number of orders made on our coffee.
We need to know which coffee has been ordered.

Both customer and coffee pointa at an order.
An order will consoist of a particular coffee, and a trace of the customer who made the order.
We need to know how many orders there are so far.

To order a coffee, a customer need to specify the coffee they are ordering.
* Our coffee would need a name!
* We would need the name of our customer
* We would need to proide a price for every coffee
-so our order would need a customer, coffee name, and a price!

-* pullying it together:

Order class seem to be our single source of truth(SSOT), an intermediary between Customer and Coffee classes.
We need to initialize an order with a customer, instance of Customer class, a coffee, instance of Coffee class and a pice.
We can have a class attribute all to keep track of all our orders.
We would need to conclude our constructor by assigning Order instance to the class attribute -all.

Customer class would need to initialize with a name.
We would need a class attribute, all, to keep track of all customer instances.
The class would need a method to create_an_order(), which will take 3 parameters. customer instance(self), coffee instance(coffee), and price.
We would need get_orders() method, that would acess orders from Order class that match the class instance. Through the order instances/objects, we can access informtion on what coffee instances the customer has ordered. We can chain name attribute to access the name of coffee that customer has ordered.

Coffee class would need to initialize with a name. 
We would need a class attribute, all, to keep track of all coffee instances.
We would need to refer to customers that order particular coffee. For this we need a customer() method. The method would retrieve this information from orders attribute in Order class. We can filter relevant orders by retrieving those that satisfy the current Cofee instance through the self keyword. Since the orders track customer instances, we can chain the customer attribute(in Order class) to retrieve customer instances that match our case.


3. Create Class Files
### prerequisite 

   - Create three Python files in your project directory:
     - `customer.py`
     - `coffee.py`
     - `order.py`

In each file, define a class corresponding to the file name (e.g., `class Customer` in `customer.py`).

### implementation

Here is how the project was created:
from the terminal:

mkdir coffee_shop
cd coffee_shop
pipenv install
pipenv shell
pipenv install pytest

touch .gitignore
touch README.md
mkdir lib

**File Structure**:
``` 
coffee_shop/
│
├── lib/
│   ├── __init__.py (empty, for lib to be treated as a proper module)
│   ├── customer.py  
│   ├── coffee.py
│   └── order.py
│
├── .gitignore
├── debug.py  
├── Pipfile / Pipfile.lock (is created by pipenv)
├── Pipfile.lock
└── README.md
```


4. Implement Initializers and Properties
### prerequisite 

   - Customer Class (`customer.py`):
     - Initialize a `Customer` with a `name` (string between 1 and 15 characters).
     - Implement a property `name` with the necessary validation.
   - Coffee Class (`coffee.py`):
     - Initialize a `Coffee` with a `name` (string, at least 3 characters long).
     - Implement a property `name` with the necessary validation.
   - Order Class (`order.py`):
     - Initialize an `Order` with a `Customer` instance, a `Coffee` instance, and a `price` (float between 1.0 and 10.0).
     - Implement properties `customer`, `coffee`, and `price` with the necessary validation.

### implementation
``` customer.py
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
    ```

Customer class is initialized with a name attribute. The @name.setter validates the name, first confirming if it is a string, then confirming if it is of the required length, and finally setting it to the name attribute.

Similar validation logic is applied for Coffee and Order classes. the property decorator is used to validate(@attribute.setter), and retrieve(@property) an instance attribute.
See below:

``` coffee.py
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
    ```

``` order.py
class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.orders.append(self)

        # ...other properties

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
    ```


5. Define Object Relationship Methods and Properties
### prerequisite 

   - Implement methods that establish relationships between objects:
     - Order Class (`order.py`):
       - `customer` property returns the `Customer` instance for the order.
       - `coffee` property returns the `Coffee` instance for the order.
     - Coffee Class (`coffee.py`):
       - `orders()` method returns a list of all `Order` instances for that coffee.
       - `customers()` method returns a unique list of `Customer` instances who have ordered that coffee.
     - Customer Class (`customer.py`):
       - `orders()` method returns a list of all `Order` instances for that customer.
       - `coffees()` method returns a unique list of `Coffee` instances that the customer has ordered.

### implementation
``` order.py
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer class")
        self._customer = customer
    ```
the customer setter validates customer attribute implementation. it accepts an argument, and validates whether it is a Customer instance. if it is, the class attribute is set to the instance as a private attribute(self._customer), notice the undescore preceding customer.

To get the customer instance, we can invoke the customer property. accessing order.customer, returns the _customer attribute (a Customer instance).

The exact same logic applies for coffee property.

``` coffee.py
    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
    ```
the orders method loops through Order classes' attribute, orders, accessing any order that matches the Coffee instance(self). customers method iterates over the list of orders, accessing each orders customer instance while capturing them in a set. The set is then converted to a list.

The above logic also applies for customer instance.
``` customer.py
    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.customer == self]
    
    def coffees(self):
        # unique list of `Coffee` instances. 
        return list({order.coffee for order in self.orders()})
    ```


6. Implement Aggregate and Association Methods
### prerequisite 

 - Customer Class (`customer.py`):
     - `create_order(coffee, price)` method: Receives a `Coffee` instance and a price, creates a new `Order` instance, and associates it with that customer and the coffee.
   - Coffee Class (`coffee.py`):
     - `num_orders()` method: Returns the total number of times a coffee has been ordered.
     - `average_price()` method: Returns the average price for a coffee based on its orders.

### implementation
``` customer.py
    def create_order(self, coffee, price): # validations will be done by Order class
        return Order(self, coffee, price)

    ```
create_order(self, coffee, price) method receives Coffee instance and a price, and initializes an order with customer instance-self, coffee-Coffee instance, and price as Order classes' constructor(__init__) parameters.

``` coffee.py
    def num_orders(self):
        return len(self.orders())
    ```
the num_orders(self) method, calls orders method- whch returns an array of orders for the current coffee instance(self), and determines the length of orders which conform to the number of orders.

``` coffee.py
    def average_price(self):
        if self.orders():
            return sum(order.price for order in self.orders()) / self.num_orders()
        return "No orders have been made yet"
    ```
the average_price(self) method, determines if orders exist/if there are any orders, self.orders() returns an array of orders. If there are orders, it iterates over them, accessing the price of each. sum() method is used to accumulate all the prices, which is divided by the number of orders. 


7. Implementing class method
### prerequisite    

    - Implement the `most_aficionado(coffee)` class method in the `Customer` class:
     - Receives a `coffee` object as an argument.
     - Returns the `Customer` instance that has spent the most money on the provided `coffee`.
     - Returns `None` if there are no customers for the provided `coffee`.

### implementation
``` customer.py
    @classmethod
    def most_aficionado(cls, coffee):
        all_customers = coffee.customers() # unique list of customers
        
        current_max_spent = 0
        highest_spender = None
        
        for customer in all_customers:
            total_spent = 0

            for order in coffee.orders(): 
                if coffee.customer == customer: # for orders specific to this customer
                   total_spent += order.price

            if total_spent > current_max_spent:
                current_max_spent = total_spent
                highest_spender = customer
            
        return highest_spender

    ```

The most_aficionado(cls, coffee) class method above:

1. Takes a Coffee instance as an input.

2. Checks all orders for the specified coffee instance.

3. Calculates the total money spent by each customer on that coffee.

4. Returns the Customer who has spent the most in total on that coffee.

5. Returns None if there are no orders for that coffee.


8. Debugging and Refactoring
### prerequisite   

Create a debug.py file to test your code interactively.
Refactor your code to improve readability and maintainability:
-Extract duplicated logic into helper methods.
-Follow Python's PEP 8 guidelines for clean and readable code.

### implementation
From your terminal, run:
``` 
python debug.py
or
python3 debug.py
```