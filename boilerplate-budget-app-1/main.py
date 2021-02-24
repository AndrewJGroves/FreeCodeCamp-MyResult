# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

"""
entertainment = budget.Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
print(str(food))
expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
print(expected)

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
"""
#print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)