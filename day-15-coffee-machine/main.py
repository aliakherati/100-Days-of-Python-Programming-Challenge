MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "pennie": 0.01,
}

def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def is_resource_sufficient(ingredients):
    """
    Check if there are sufficient resources to make the drink.
    
    Args:
        ingredients (dict): A dictionary of ingredients required for the drink.
    
    Returns:
        bool: True if there are sufficient resources, False otherwise.
    """
    is_enough = True
    insufficient_resources = []
    for item, amount in ingredients.items():
        if resources[item] < amount:
            insufficient_resources.append(item)
    if insufficient_resources:
        print(f"Sorry, there is not enough {', '.join(insufficient_resources)}.")
        is_enough = False
    return is_enough

def process_coins():
    """returns the total calculated by coins inserted"""
    global coins
    total = 0
    for coin, value in coins.items():
        total += int(input(f"How many {coin}s?: ")) * value
    return total

def is_transaction_successful(payment, drink_cost):
    global profit
    payment = round(payment, 2)
    print(f"${payment} is inserted.")
    if payment < drink_cost:
        print(f"Sorry that's not enough money! ${payment} refunded.")
        return False
    profit += drink_cost
    change = round(payment - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    return True


def process_order(choice):
    global resources, profit
    drink = MENU[choice]
    ingredients = drink["ingredients"]
    
    # Check if there are enough resources
    if not is_resource_sufficient(ingredients):
        return False
    
    # Process coins
    payment = process_coins()
    if not is_transaction_successful(payment, drink["cost"]):
        return False
    
    # If we have enough resources, deduct them
    for item, amount in ingredients.items():
        resources[item] -= amount
    
    # For now, we'll assume the payment is always successful
    profit += drink["cost"]
    
    print(f"Here is your {choice}. Enjoy! ☕️")
    return True

def coffee_machine():
    is_on = True
    while is_on:
        user_choice = prompt_user()
        
        if user_choice == "off" or user_choice == "stop":
            is_on = False
            print("Turning off the coffee machine. Goodbye!")
        elif user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif user_choice in MENU:
            print(f"You ordered {user_choice}.")
            process_order(user_choice)
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    coffee_machine()
