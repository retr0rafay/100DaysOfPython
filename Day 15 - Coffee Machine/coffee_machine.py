MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}

# Run the coffee machine
def coffeeMachine():
  global MENU
  global resources
  while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "off":
      print("Powering off the coffee machine...")
      break
    elif coffee_type == "report":
      printReport()
      continue
    if getDrink(coffee_type):
      askFunds(MENU[coffee_type]["cost"], coffee_type)
    else:
      continue

# Print the report
def printReport():
  global resources
  print(f'Water: {resources["water"]}ml')
  print(f'Milk: {resources["milk"]}ml')
  print(f'Coffee: {resources["coffee"]}ml')
  print(f'Money: ${resources["profit"]}')

def getDrink(coffee_type):
  global resources
  if enoughResources(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    if coffee_type == "latte" or coffee_type == "cappuccino":
      resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    return True
  else:
    return False

def enoughResources(coffee_type):
  global resources
  global MENU
  enough_water = resources["water"] > MENU[coffee_type]["ingredients"]["water"]
  enough_milk = 0
  if coffee_type == "latte" or coffee_type == "cappuccino":
    enough_milk = resources["milk"] > MENU[coffee_type]["ingredients"]["milk"]
  enough_coffee = resources["coffee"] > MENU[coffee_type]["ingredients"]["coffee"]
  if not enough_water:
    print("Sorry there is not enough water")
    return False
  elif not enough_milk and (coffee_type == "latte" or coffee_type == "cappuccino"):
    print("Sorry there is not enough milk")
    return False
  elif not enough_coffee:
    print("Sorry there is not enough coffee")
    return False
  else:
    return True

def askFunds(coffee_cost, coffee_type):
  global resources
  print("Please insert coins.")
  num_quarters = int(input("How many quarters?: "))
  num_dimes = int(input("How many dimes?: "))
  num_nickles = int(input("How many nickles?: "))
  num_pennies = int(input("How many pennies?: "))
  total_amount = (num_quarters * .25) + (num_dimes * .1) + (num_nickles * .05) + (num_pennies * .01)
  if total_amount < coffee_cost:
    print("Sorry that's not enough money. Money refunded")
  elif total_amount > coffee_cost:
    resources["profit"] += coffee_cost
    change_amount = round(total_amount - coffee_cost, 2)
    print(f'Here is your ${change_amount} change!')
    print(f'Here is your {coffee_type} ☕️  Enjoy!')
  elif total_amount == coffee_cost:
    resources["profit"] += coffee_cost
    print(f'Here is your {coffee_type} ☕️  Enjoy!')

coffeeMachine()
