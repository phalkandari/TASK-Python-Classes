class Wallet:
    def __init__(self,money):
        self.money = money

    def credit(self, amount):
        total_addition = amount + self.money
        print (f"The new amount of money is {total_addition}")

    def debit(self, amount):
        self.amount = amount
        total_subtraction = self.money - self.amount
        print (f"The new amount of money is {total_subtraction}")


wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(wallet)


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
