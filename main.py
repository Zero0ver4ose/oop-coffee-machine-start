from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

game_start = True
make_coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while game_start:
    options = menu.get_items()
    userinput = input(f"What would yoou like? ({options})?: ")
    if userinput == "off":
        game_start = False
    elif userinput == "report":
        make_coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(userinput)
        if make_coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                make_coffee.make_coffee(drink)











