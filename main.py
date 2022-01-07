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


def make_drink(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    print(f"Here is your {drink} ☕️. Enjoy!")


def transaction_successful(money, drink):
    """A boolean function that check if the user has insert enough money"""
    if money < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money > MENU[drink]["cost"]:
        print(f"Here is ${round(money - MENU[drink]['cost'], 2)} dollars in change.")
        return True
    else:
        return True


def resources_sufficient(drink):
    """A boolean function that takes a drink and check whether there are enough resources
        in the machine to make that drink."""
    sufficient = False
    if (drink == "latte" or drink == "cappuccino") and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry, there's not enough milk.")
    elif resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there's not enough water.")
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there's not enough coffee.")
    else:
        sufficient = True

    return sufficient


def insert_coins():
    """A function that ask the user to insert the coins and return the total amount of money inserted"""
    # TODO handle the case where the user enter non int
    coins = {"quarters($0.25)": 0, "dimes($0.10)": 0, "nickles($0.05)": 0, "pennies($0.10)": 0}
    print("Please insert coins.")
    for coin in coins:
        coins[coin] = int(input(f"How many {coin} : "))
    return (coins["quarters($0.25)"] * 0.25) +\
           (coins["dimes($0.10)"] * 0.1) +\
           (coins["nickles($0.05)"] * 0.05) +\
           (coins["pennies($0.10)"] * 0.01)


machine_on = True
money_in_the_machine = 0

while machine_on:
    # Get the user choice
    choice = input("\nWhat would you like? [Espresso($1.5), Latte($2.5), Cappuccino($3.0)? ").lower()
    if choice == "off":
        print("The machine is turned off. Good bye!")
        machine_on = False
    elif choice == "report":
        print("Here's the report:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_in_the_machine}")
    elif choice in MENU.keys():
        print(f"You chose {choice} and it costs ${MENU[choice]['cost']}")
        # We check if the resources are sufficient
        if resources_sufficient(choice):
            # We ask the user to insert coins
            money_inserted = insert_coins()
            # We remind the user how much he inserted
            print(f"You inserted ${money_inserted}")
            if transaction_successful(money_inserted, choice):
                money_in_the_machine += MENU[choice]["cost"]
                make_drink(choice)

    else:
        # We handle the cases where the user enter a drink not offered.
        print("Enter a valid drink.")


# Coffee Machine Program Requirements

# Done
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#   a. Check the user’s input to decide what to do next.
#   b. The prompt should show every time action has completed, e.g. once the drink is
#   dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
#   a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#   the machine. Your code should end execution when this happens.
# 3. Print report.
#   a. When the user enters “report” to the prompt, a report should be generated that shows
#   the current resource values. e.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
# 4. Check resources sufficient?
#   a. When the user chooses a drink, the program should check if there are enough
#   resources to make that drink.
#   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#   not continue to make the drink but print: “Sorry there is not enough water.”
#   c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
#   a. If there are sufficient resources to make the drink selected, then the program should
#   prompt the user to insert coins.
#   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#   pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
#   a. Check that the user has inserted enough money to purchase the drink they selected.
#   E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#   program should say “Sorry that's not enough money. Money refunded.”.
#   b. But if the user has inserted enough money, then the cost of the drink gets added to the
#   machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#   c. If the user has inserted too much money, the machine should offer change.
#   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#   places.
# 7. Make Coffee.
#   a. If the transaction is successful and there are enough resources to make the drink the
#   user selected, then the ingredients to make the drink should be deducted from the
#   coffee machine resources.
#   E.g. report before purchasing latte:
#   Water: 300ml
#   Milk: 200ml
#   Coffee: 100g
#   Money: $0
#   Report after purchasing latte:
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#   b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#   latte was their choice of drink.
