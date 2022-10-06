from turtle import distance


class Wallet:
    """A simple wallet to keep track of money."""

    def __init__(self, money=0):  # default the value for money to 0
        self.money = money

    def __str__(self):  # This method returns the string representation of the object
        return f"This wallet has {self.money}"

    def credit(self, amount):
        """
        Adds the amount to the money attribute,
        then prints the new value
        """
        self.money = self.money + amount
        print(f"Credit: The new amount of money is {self.money}")

    def debit(self, amount):
        """
        Subtracts the amount from the money attribute,
        then prints the new value
        """
        self.money = self.money - amount
        print(f"Debit: The new amount of money is {self.money}")


wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0

wallet_instance = Wallet(0)


class Person:
    """A simple person class"""

    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)

    def moveTo(self, point):
        self.location = point
        print(f"The new location of {self.name} is {self.location}")


person = Person("Moh", 5, 50)


class Vendor(Person):
    """A subclass of Person with the job Vendor"""

    def _init__(self, name, location, money):
        super().__init(name, location, money)
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams):
        """
        sells a specific number of ice creams to the customer:
        Moves to the customer's location,
        Transfers money from the customer's wallet to the vendor's wallet,
        Prints a nice message saying how many icecreams were sold
        """
        self.location = customer.location
        self.wallet.credit(number_of_icecreams * self.price)
        customer.wallet.debit(number_of_icecreams * self.price)


vendor = Vendor("Abdallah", 3, 6)


class Customer(Person):
    """A simple customer class."""

    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def is_in_range(self, vendor):
        distance = vendor.location - self.location
        if distance > vendor.range:
            return True
        else:
            return False

    def have_enough_money(self, vendor, number_of_icecreams):
        if self.wallet.money >= vendor.price * number_of_icecreams:
            return True
        else:
            return False

    def request_icecream(self, vendor, number_of_icecreams):
        if self.is_in_range(vendor) and self.have_enough_money(
            vendor, number_of_icecreams
        ):
            vendor.sellTo(self, number_of_icecreams)


customer = Customer("Abdallah", 3, 6)
