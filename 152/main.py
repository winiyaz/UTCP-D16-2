# Section 152

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Setting up the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Calling the reports
coffee_maker.report()
money_machine.report()

