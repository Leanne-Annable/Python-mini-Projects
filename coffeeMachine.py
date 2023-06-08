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
    },
    "water": {
        "ingredients": {
            "water": 300,
        },
        "cost": 1.0,
    },
}

profit = 0
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 150,
}


# TODO: 4. Check resources sufficient?
# TODO: 4.1. When drink selected, check enough resources available to make drink
# TODO: 4.2. If a resource is too low alert user "Sorry there is not enough -- ."
# TODO: 4.3. Alert should be available for all resources.
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins.
# TODO: 5.1. If sufficient resources, program should prompt user to insert coins.
# TODO: 5.2. £1, 50p, 20, 10, 5.
# TODO: 5.3. calculate the monetary value of coins inserted, number x value of each coin.
def process_coins():
    """Returns the total sum of the coins"""
    print("Please insert coins")
    total = int(input("How many pounds: "))
    total += int(input("How many 50p's: ")) * 0.5
    total += int(input("How many 20p's: ")) * 0.2
    total += int(input("How many 10p's: ")) * 0.1
    total += int(input("How many 5p's: ")) * 0.05
    return total


# TODO: 6. Check user has inserted enough money to purchase drink, coins >= cost.
# TODO: 6.1. If user hasn't inserted enough money program should alert user and not add total coin amount.
# TODO: 6.2. If enough money inserted, cost of drink added to profits in report.
# TODO: 6.3. If user inserts too much money, machine should offer change to 2dp.

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is £{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make Coffee.
# TODO: 7.1. When transaction successful, ingredients used should be deducted from report total.
# TODO: 7.2. When resources have been deducted, tell user "Here is you --. Enjoy!"
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : £{profit}")
    refill = input("Would you like to refill the machine? (Y/N)").upper()
    if refill == "Y":
        resources['water'] = 1000
        resources['milk'] = 500
        resources['coffee'] = 150
    else:
        return


is_on = True
print("Welcome to your coffee machine!")
print("Here is a list of extra commands you may request other than your coffee order:")
print("'report' - This gives a report of the ingredient levels within the machine and gives you the option ro refill.")
print("'off' - This turns the machine off.")
print("Now for your order!")


while is_on:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):".
    # TODO: 1.1. Check users input to decide what to do next.
    # TODO: 1.2. The prompt should show every time a drink has been dispensed, to serve the next customer.
    choice = input("What would you like? (espresso/latte/cappuccino/water):").lower()
    # TODO: 2. Turn off the coffee machine by entering "off" to the prompt. Thus ending the code execution.
    if choice == "off":
        is_on = False
    # TODO: 3. Print Report.
    # TODO: 3.1. When user enters "report" to the prompt, a report generated showing all remaining values and levels
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])





