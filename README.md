# Coffee Shop Domain Modeling
## Objective
The goal is to simulate a coffee shop domain by building a Python application from scratch. The implementations follow the guidelines of object-oriented programming. The project demonstrates the capacity to create classes, put methods into practice, create object relationships, and manage data properly.

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

<u>**Pseudocode**</u>

\- The domain model for the coffee shop includes: 
customers, coffee, and orders.  
A customer engages with the shop by placing an order.  
A customer places an order for coffee.  
A customer has the ability to order multiple coffees.  
Coffee is requested by the customer.  
In order for coffee to be ordered, a customer must be present.   
We need to track who is ordering our coffee.  
We need to monitor the total number of orders made for our coffee.  
We need to identify which coffees have been ordered.

Both the customer and the coffee are involved in an order.  
An order consists of a specific type of coffee and details about the customer who placed it.  
We need to keep track of the total number of orders made so far.

To place a coffee order, a customer must indicate which coffee they want.  
* Each coffee needs to have a name!  
* We also need the name of the customer.  
* Additionally, we must provide a price for each coffee; thus, our order should include a customer, coffee name, and the price!

\-<u>__pullying it together__**:**</u>

The **Order** class acts as our sole **source of truth** (SSOT), serving as a mediator(intermediary) between the Customer and Coffee classes.  
We should create an order by providing it with a customer, which is an instance of the Customer class, a coffee, represented by an instance of the Coffee class, and a price.  
We can introduce a class attribute called `all` to track all of our orders.  
Lastly, we need to complete our constructor by assigning the Order instance to the `all` class attribute.

The Customer class should be initialized with a name.  
We will require a class attribute, `all`, to track all instances of customers.  
The class needs a method called `create_an_order()`, which accepts three parameters: the customer instance (self), a coffee instance (coffee), and the price.  
Additionally, we will need a method called `get_orders()` that will retrieve orders from the Order class corresponding to the specific customer instance. By accessing the order instances/objects, we can obtain details about which coffee instances the customer has ordered. We can chain the name attribute to find out the names of the coffees ordered by the customer.

The Coffee class should be initialized with a name.  
We require a class attribute, all, to monitor all coffee instances.  
We need to identify customers that place orders for specific coffee. To achieve this, we need a `customer()` method. This method will gather the information from the orders attribute in the Order class.  
We can filter the relevant orders by selecting those that meet the criteria of the current Coffee instance using the self keyword. Since the orders keep track of customer instances, we can chain the customer attribute in the Order class to obtain customer instances that correspond to our situation.


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

The Customer class is initialized with a name property. The @name.setter checks the name by first verifying that it is a string, then ensuring it meets the necessary length, and ultimately assigning it to the name attribute. 

Comparable validation logic is utilized for the Coffee and Order classes. The property decorator is employed to validate (@attribute.setter) and access (@property) an instance attribute.
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
The customer setter validates customer attribute implementation. It accepts an argument and validates whether it is a Customer instance. If it is, the class attribute is set to the instance as a private attribute(self._customer). Notice the underscore preceding customer.

To get the customer instance, we can invoke the customer property. Accessing order.customer, yields/returns the _customer attribute (a Customer instance).

The same logic applies to coffee property.

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

## Conclusion

This Coffee Shop domain model demonstrates the principles of object-oriented programming, including encapsulation, relationships, validation, and aggregation. By modeling real-world entities like customers, coffees, and orders, the system provides a clean and extensible foundation for managing coffee shop operations. The project is structured for clarity and maintainability, making it easy to expand with additional features such as persistence, a user interface, or integration with a backend API.