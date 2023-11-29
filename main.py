from menu import MENU, resources

profit = 0



def is_resources_sufficient(order_ingridients):
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input('how many quarters')) * 0.25
    total += int(input('how many dimes')) * 0.1
    total += int(input('how many nickles')) * 0.05
    total += int(input('how many pennies')) * 0.01
    return total



def is_transaction_succesful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingridients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {drink_name} ☕")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        break
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

