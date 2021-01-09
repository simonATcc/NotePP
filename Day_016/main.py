from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker=CoffeeMaker()
machine=MoneyMachine()
while True:
    coffee_type=input("What would you like? (espresso/latte/cappuccino):")
    if coffee_type=="off":
        exit()
    elif coffee_type =="report":
        maker.report()
        machine.report()
    else:
        menu=Menu()
        drink:MenuItem=menu.find_drink(coffee_type)
        if not maker.is_resource_sufficient(drink):
            print(f"Sorry there is not enough material")
            continue
        if not machine.make_payment(drink.cost):
            continue
        maker.make_coffee(drink)
