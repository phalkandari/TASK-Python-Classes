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


# class Person:
#     name = "X"
#     location = "Y"
#     wallet = "Z"

#     def moveTo(self, point):
#         self.location = point
#         print (f"Your new location is {self.location}")


# person = Person("Moh", 5, 50)


# class Vendor:
#     # implement Vendor!
#     pass


# vendor = Vendor("Abdallah", 3, 6)


# class Customer:
#     # implement Customer!
#     pass


# customer = Customer("Abdallah", 3, 6)
