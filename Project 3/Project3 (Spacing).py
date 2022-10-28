# This is the start of the script code for Project 3 by Tyler Pham and Parth Balchandani created in 10/21/2022.

# Stock of Coins and Dollars
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

# Print welcome message for start of the program
print("\nWelcome to the vending machine change maker program\nChange maker initialized.")


def stock():  # Function that displays stock amounts
    print("Stock contains: ")
    print(f"\t{nickels} nickles")
    print(f"\t{dimes} dimes")
    print(f"\t{quarters} quarters")
    print(f"\t{ones} ones")
    print(f"\t{fives} fives\n")


def menu():  # Function that displays the menu
    print("\nMenu for deposits: ")
    print("\t\'n\' - deposit a nickel")
    print("\t\'d\' - deposit a dime")
    print("\t\'q\' - deposit a quarter")
    print("\t\'o\' - deposit a one dollar bill")
    print("\t\'f\' - deposit a five dollar bill")
    print("\t\'c\' - cancel the purchase\n")


def payment_due(total_cents):  # Function that displays payment due
    bills = int(total_cents / 100)
    coins = int(total_cents % 100)
    if bills >= 1:
        print(f"Payment due: {bills} dollar(s) and {coins} cents")
    else:
        print(f"Payment due: {coins} cents")


def change_due(total_cents):  # Function that displays the amount of change left if there are no more coins.
    bills = int(total_cents / 100)
    coins = int(total_cents % 100)
    if bills >= 1:
        print(f"Amount due is: {bills} dollar(s) and {coins} cents")
    else:
        print(f"Amount due is: {coins} cents")


def total(total_amount):  # Function that displays total amount of money in stock; The final amount.
    bills = int(total_amount / 100)
    coins = int(total_amount % 100)
    if bills >= 1:
        print(f"\nTotal: {bills} dollar(s) and {coins} cents")
    else:
        print(f"\nTotal: {coins} cents")


stock()
price_input = input("Enter the purchase (xx.xx) or \'q\' to quit: ")
while price_input != 'q':
    price_input = float(price_input)
    price_as_whole = round(price_input * 100)
    # Price Verification
    if (price_as_whole < 0) or (price_as_whole % 5 != 0):
        print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
        price_input = input("Enter the purchase (xx.xx) or \'q\' to quit: ")
        continue
    menu()
    # Deposit
    deposit_input = 0
    while deposit_input != 'c' and price_as_whole > 0:
        payment_due(price_as_whole)
        deposit_input = input("Indicate your deposit: ")
        if deposit_input == 'n':  # Deposits 1 nickel and adds it to stock
            price_as_whole -= 5
            nickels += 1
        elif deposit_input == 'd':  # Deposits 1 dime and adds it to stock
            price_as_whole -= 10
            dimes += 1
        elif deposit_input == 'q':  # Deposits 1 quarter and adds it to stock
            price_as_whole -= 25
            quarters += 1
        elif deposit_input == 'o':  # Deposits 1 one-dollar bill and adds it to stock
            price_as_whole -= 100
            ones += 1
        elif deposit_input == 'f':  # Deposits 1 five-dollar bill and adds it to stock
            price_as_whole -= 500
            fives += 1
        elif deposit_input == 'c':  # Cancels the entire payment
            price_as_whole -= round(price_input * 100)
        else:  # Detects bad inputs
            print(f"Illegal selection: {deposit_input}")
    # Change determined from price as a whole
    change = abs(price_as_whole)
    print("\nPlease take the change below.")
    if change != 0:
        while change > 0:
            quarters_change = change // 25
            dimes_change = change // 10
            nickels_change = change // 5
            if quarters != 0 and change >= 25:
                if quarters < quarters_change:
                    quarters_change = quarters
                change -= 25 * quarters_change
                quarters -= quarters_change
                print(f"\t{quarters_change} quarters")
            elif dimes != 0 and change >= 10:
                if dimes < dimes_change:
                    dimes_change = dimes
                change -= 10 * dimes_change
                dimes -= dimes_change
                print(f"\t{dimes_change} dimes")
            elif nickels != 0 and change >= 5:
                if nickels < nickels_change:
                    nickels_change = nickels
                change -= 5 * nickels_change
                nickels -= nickels_change
                print(f"\t{nickels_change} nickels")
            else:
                print("Machine is out of change.\nSee store manager for remaining refund.")
                change_due(change)
                change = 0
    else:
        print("\tNo change due.")
    # Restart
    print()
    stock()
    price_input = input("Enter the purchase (xx.xx) or \'q\' to quit: ")

totals = (nickels * 5) + (dimes * 10) + (quarters * 25) + (ones * 100) + (fives * 500)
total(totals)
