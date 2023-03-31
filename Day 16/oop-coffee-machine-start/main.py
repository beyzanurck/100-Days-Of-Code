from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while True:
    requested_coffee = input(f"What would you like? {menu.get_items()}: ").lower()       
    
    if requested_coffee == "report":
        coffee_maker.report()
        continue      

    item = menu.find_drink(requested_coffee)
    
    if (coffee_maker.is_resource_sufficient(item)):

        if money.make_payment(item.cost):
            coffee_maker.make_coffee(item)


