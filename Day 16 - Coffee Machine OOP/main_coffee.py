from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

rafay_menu = Menu()
salesforce_coffee_maker = CoffeeMaker()
salesforce_coffee_maker_money_machine = MoneyMachine()

while True:
  order_name = input(f"What would you like? ({rafay_menu.get_items()}): ").lower()
  if order_name == "off":
    break
  elif order_name == "report":
    salesforce_coffee_maker.report()
    salesforce_coffee_maker_money_machine.report()
    continue
  drink = rafay_menu.find_drink(order_name)
  if salesforce_coffee_maker.is_resource_sufficient(drink):
    salesforce_coffee_maker_money_machine.make_payment(drink.cost)
    salesforce_coffee_maker.make_coffee(drink)
  else:
    continue
