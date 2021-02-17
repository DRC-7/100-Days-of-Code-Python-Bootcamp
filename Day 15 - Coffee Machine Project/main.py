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
}


def run_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: {resources["money"]}')


def check_resources(selection):
    for i in MENU[selection]["ingredients"]:
        required_amt = MENU[selection]["ingredients"][i]
        if resources[i] < required_amt:
            print(f'Sorry there is not enough {i}')
            return False
        else:
            return True


def count_user_coins():
    print("Please enter the amount of coins you have...")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total_value = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f'Total value of coins: ${total_value:.2f}')
    return total_value


def check_transaction(avail_money, selection):
    required_amt = MENU[selection]['cost']
    change = 0
    if avail_money < required_amt:
        change += avail_money
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        change = avail_money - required_amt
        print(f'Here is ${change:.2f} in change')
    return change


def make_coffee(selection):
    for key in resources:
        MENU[selection]["ingredients"].setdefault(key)
        if MENU[selection]["ingredients"][key] is not None:
            resources[key] -= MENU[selection]["ingredients"][key]
    resources["money"] += MENU[selection]["cost"]


# MAIN
run_coffee_machine = True
resources["money"] = 0
while run_coffee_machine is True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        run_coffee_machine = False
    elif user_input == "report":
        run_report()
    else:
        if check_resources(user_input) is True:
            user_money = count_user_coins()
            user_money -= check_transaction(user_money, user_input)
            make_coffee(user_input)
            if user_input == "latte":
                print("Here is your latte. Enjoy!\n")
        else:
            pass
