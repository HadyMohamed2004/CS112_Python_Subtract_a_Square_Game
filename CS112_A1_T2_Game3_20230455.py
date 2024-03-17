"""
File: CS112_A1_T2_2_20230455.py
Purpose:    Subtract a square. This is a two-player mathematical game of strategy. It is played by two
            people with a pile of coins (or other tokens) between them. The players take turns removing
            coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
            The player who removes the last coin wins.
Course: Structured Programming - CS112
Author: Hady Mohammed Meawad Mohammed
ID: 20230455
"""

"""
Game 3, Task 2, Assignment 1 --> Subtract a square


"""


# Check if square of the number is a non-zero positive number and its square is less than remaining coins
def is_square(num, coins):
    if num <= 0:  # if 0 is entered --> Invalid
        return False
    return num ** 0.5 == int(num ** 0.5) and num <= coins



# Function to Check if User Input is an Integer
def get_integer_input(prompt):
    while True:
        # Try to convert the input to an integer and return its Value
        try:
            value = int(input(prompt))
            return value
        # If the input is not an integer, print a message and try again
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Game Instructions
print("Welcome to Subtract a Square Game")
print("This is a two-player mathematical game of strategy.")
print("It is played by two people with a pile of coins (or other tokens) between them.")
print(
    "The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).")
print("The player who removes the last coin wins.")
print("-------------------------------------------------------------------------------------------------")

# Initialize Current player
current_player = 1

# Get Starting Pile of Coins from User
while True:
    coins = get_integer_input("Enter the starting amount of coins: ")
    if coins <= 0:
        print("Invalid input. Please enter a positive amount of coins.")
    else:
        break

# Game Loop
while True:
    # Divider, To Divide between Player 1 and Player 2
    print("-------------------------------------------------------------------------------------------------")

    # Display Remaining Pile of Coins
    print("Coins left: ", coins)

    # Prompt User to enter an Integer and Check if it's valid (non-zero, its square is less than remaining coins and it's ok to be 1)
    while True:
        n = get_integer_input(f"Player {current_player}, Enter a number: ")
        if is_square(n, coins):
            break
        else:
            print("Invalid number, try again.")

    # Remove the Square of the Number from the Pile of Coins
    coins = coins - n

    # Check if the Pile of Coins is Empty
    if coins == 0:
        # Display Winner
        print(f"Player {current_player} wins")
        break

    # Switch Current Player, Using Relative relation between 1,2,3, Player 1 --> 3-1=2 --> Change player to 2
    current_player = 3 - current_player
