# Section 152
'''
This is similar to this
https://github.com/K0unty/utcp1/blob/main/WORK/D15/D15.ipynb
- This being converted into OOB
'''

from rich.prompt import Prompt as pro
from rich import print as rprint
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Object instantiation
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


# Calling the reports
coffee_maker.report()
money_machine.report()

# For running the while loop
is_on = True

while is_on:
	options = menu.get_items()
	choice = pro.ask(f'What you want? ({options})', default="off")
	if choice == 'off':
		is_on = False
	elif choice == 'report':
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(choice)
		if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
			coffee_maker.make_coffee(drink)