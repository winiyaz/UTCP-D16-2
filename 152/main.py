# Section 152
'''
This is similar to this
https://github.com/K0unty/utcp1/blob/main/WORK/D15/D15.ipynb
- This being converted into OOB
'''
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Setting up the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Calling the reports
coffee_maker.report()
money_machine.report()

