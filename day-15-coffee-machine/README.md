# Coffee Machine Program Objectives

1. **User Interaction**
   - Prompt user with: "What would you like? (espresso/latte/cappuccino): "
   - Display prompt after each action to serve the next customer

2. **Machine Control**
   - Turn off the machine when "off" is entered (secret maintenance command)

3. **Resource Reporting**
   - Print a report of current resources when "report" is entered
   - Display water, milk, coffee levels, and money earned

4. **Resource Management**
   - Check if there are sufficient resources for the selected drink
   - Inform user if a resource is depleted

5. **Payment Processing**
   - Prompt for coin insertion if resources are sufficient
   - Calculate total monetary value of inserted coins
   - (quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01)

6. **Transaction Handling**
   - Verify if inserted money is sufficient for the selected drink
   - Refund money if insufficient
   - Add payment to profit if transaction is successful
   - Offer change if too much money is inserted (rounded to 2 decimal places)

7. **Beverage Preparation**
   - Deduct used ingredients from machine resources
   - Confirm drink delivery to the user
