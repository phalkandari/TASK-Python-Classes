class Wallet:
    """A simple wallet to keep track of money."""
    def __init__(self, money):
        self.money = money

    def credit(self, amount):
        """
        Adds the amount to the money attribute,
        then prints the new value
        """
        self.money = self.money + amount
        print (f"The new amount of money is {self.money}")

    def debit(self, amount):
        """
        Subtracts the amount from the money attribute,
        then prints the new value
        """
        self.money = self.money - amount
        print (f"The new amount of money is {self.money}")


wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(wallet.credit(5))
print(wallet.debit(3))

wallet_instance = Wallet(0)


class Person:
    """A simple person class"""
    def __init__(self, name, location, wallet):
        self.name = name
        self.location = location
        self.wallet = wallet_instance.credit(wallet)

    def moveTo(self, point):
        self.location = point
        print (f"Your new location is {self.location}")


person = Person("Moh", 5, 50)


class Vendor(Person):
    """A subclass of Person with the job Vendor"""
    def _init__(self, name, location, wallet):
        super().__init(name, location, wallet)
        self.range = 5
        self.price = 1
    
    def sellTo(customer, number_of_icecreams):
        """
        sells a specific number of ice creams to the customer:
        Moves to the customer's location,
        Transfers money from the customer's wallet to the vendor's wallet,
        Prints a nice message saying how many icecreams were sold        
        """
        




vendor = Vendor("Abdallah", 3, 6)


# class Customer:
#     # implement Customer!
#     pass


# customer = Customer("Abdallah", 3, 6)
