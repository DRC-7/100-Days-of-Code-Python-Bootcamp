from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

run_machine = True
while run_machine:
    options = menu.get_items()
    user_input = input(f'What would you like? ({options}): ').lower()
    if user_input == 'off':
        run_machine = False
    elif user_input == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        select = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(select) and money_machine.make_payment(select.cost):
            coffee_machine.make_coffee(select)
