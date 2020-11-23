import random


# take in a number 0 - 2 from the user that represents their hand

userHand = int(input("What's your hand? 0=Rock, 1=Paper, 2=Scissors: "))

# generate a random number 0 - 2 to use for the computer's hand

computerHand = random.randint(0, 2)

# call the function get_hand to get the string representation of the user's hand


def get_hand(hand):
    hands = {0: "Rock", 1: "Paper", 2: "Scissors"}
    return hands[hand]


userPlays = get_hand(userHand)

# call the function get_hand to get the string representation of the computer's hand

computerPlays = get_hand(computerHand)

# call the function determine_winner to figure out who won


def determine_winner():
    if userHand == 0 and computerHand == 2\
            or userHand == 1 and computerHand == 0\
            or userHand == 2 and computerHand == 1:
        winner = "You!"
    elif userHand == computerHand:
        winner = "It's a tie!"
    else:
        winner = "The computer!"
    return winner


# print out the player hand and computer hand

print(f"\nPlayer plays {userPlays}, Computer plays {computerPlays}")

# print out the winner

print(f"\nAnd the winner is... {determine_winner()}")
