import json
from typing import Dict, Any

# Load configuration from JSON file
with open('./config.json', 'r') as config_file:
    config: Dict[str, Any] = json.load(config_file)

MENU: Dict[str, Dict[str, Any]] = config['MENU']
INITIAL_RESOURCES: Dict[str, int] = config['INITIAL_RESOURCES']
COINS: Dict[str, float] = config['COINS']

class CoffeeMachine:
    def __init__(self) -> None:
        """Initialize the coffee machine with initial resources and zero profit."""
        self.profit: float = 0
        self.resources: Dict[str, int] = INITIAL_RESOURCES.copy()

    def prompt_user(self) -> str:
        """
        Prompt the user for their drink choice.
        
        Returns:
            str: The user's drink choice in lowercase.
        """
        return input("What would you like? (espresso/latte/cappuccino): ").lower()

    def is_resource_sufficient(self, ingredients: Dict[str, int]) -> bool:
        """
        Check if there are sufficient resources to make the drink.
        
        Args:
            ingredients (Dict[str, int]): A dictionary of ingredients required for the drink.
        
        Returns:
            bool: True if there are sufficient resources, False otherwise.
        """
        insufficient_resources: List[str] = [item for item, amount in ingredients.items() if self.resources[item] < amount]
        if insufficient_resources:
            print(f"Sorry, there is not enough {', '.join(insufficient_resources)}.")
            return False
        return True

    def process_coins(self) -> float:
        """
        Process the coins inserted by the user.
        
        Returns:
            float: The total amount of money inserted, rounded to 2 decimal places.
        """
        total: float = sum(int(input(f"How many {coin}s?: ")) * value for coin, value in COINS.items())
        return round(total, 2)

    def is_transaction_successful(self, payment: float, drink_cost: float) -> bool:
        """
        Check if the payment is sufficient for the drink and handle the transaction.
        
        Args:
            payment (float): The amount paid by the user.
            drink_cost (float): The cost of the selected drink.
        
        Returns:
            bool: True if the transaction is successful, False otherwise.
        """
        if payment < drink_cost:
            print(f"Sorry that's not enough money. ${payment:.2f} refunded.")
            return False
        change: float = round(payment - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        self.profit += drink_cost
        return True

    def make_coffee(self, drink_name: str, ingredients: Dict[str, int]) -> None:
        """
        Make the coffee by deducting the required ingredients from resources.
        
        Args:
            drink_name (str): The name of the drink being made.
            ingredients (Dict[str, int]): A dictionary of ingredients required for the drink.
        """
        for item, amount in ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {drink_name}. Enjoy! ☕️")

    def process_order(self, choice: str) -> None:
        """
        Process the user's order.
        
        Args:
            choice (str): The user's drink choice.
        """
        drink: Dict[str, Any] = MENU[choice]
        if not self.is_resource_sufficient(drink["ingredients"]):
            return
        payment: float = self.process_coins()
        if self.is_transaction_successful(payment, drink["cost"]):
            self.make_coffee(choice, drink["ingredients"])

    def print_report(self) -> None:
        """Print a report of the current resource levels and profit."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.profit:.2f}")

    def run(self) -> None:
        """Run the coffee machine, handling user interactions and orders."""
        while True:
            choice: str = self.prompt_user()
            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                break
            elif choice == "report":
                self.print_report()
            elif choice in MENU:
                self.process_order(choice)
            else:
                print("Invalid selection. Please try again.")

if __name__ == "__main__":
    coffee_machine: CoffeeMachine = CoffeeMachine()
    coffee_machine.run()
