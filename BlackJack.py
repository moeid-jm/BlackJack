# BlackJack V1.0
# Hope you enjoy it :)

import random
from art import logo

def game_engine():

    user_hand = []
    computer_hand = []

    # Using the card_dealer function to draw cards for each player
    card_dealer(user_hand)
    card_dealer(computer_hand)
    card_dealer(user_hand)
    card_dealer(computer_hand)

    print(f"\nYour cards: {user_hand}")
    print(f"\nComputer\'s first card: {computer_hand[0]}")

    # Using a Loop for communicate with the dealer
    in_game = True

    while in_game:

        if input("\nDo you want another card:(Y/N) ").lower() == 'y':
            card_dealer(user_hand)
            print(f"\nYour cards: {user_hand}")


        else:
            print("\n**********************************")

            # Check for Ace card to change the value to 1 in user hand
            # If the user score is above 21 then the value of Ace card will change
            user_score = score_calculator(user_hand)
            updated_user_hand = ace_checker(user_hand, user_score)
            updated_user_score = score_calculator(updated_user_hand)

            print(f"Your final hand is: {updated_user_hand}")
            print(f"(Your score: {updated_user_score})\n")

            # At the beginning of the round the computer must have 2 cards
            # if the score is below then 17 computer must pick another card
            computer_score = score_calculator(computer_hand)
            updated_computer_hand = computer_hand_updater(computer_hand, computer_score)
            updated_computer_score = score_calculator(updated_computer_hand)

            print(f"\nComputer\'s final hand is: {updated_computer_hand}")
            print(f"(Computer\'s score: {updated_computer_score})\n")

            # Compare both scores and find the winner of the game
            in_game = pick_winner(updated_user_score, updated_computer_score)

            # Using new_game function to play another round
            new_game()


def card_dealer(side):
    """Give one card to chosen side and update the deck"""

    suit_name, suit_card = random.choice( list( card_deck.items() ) )
    random_card = random.choice(card_deck[suit_name])
    side.append(random_card)
    card_deck[suit_name].remove(random_card)


def score_calculator(hand):
    """Calculate and return the score base on player hand"""

    score = 0

    for card in hand:
        score += card

    return score


def ace_checker(gamer_hand, gamer_score):
    """Check if there is an Ace in hand and the score is 21 to change the Ace value to (1)"""

    if 11 in gamer_hand and gamer_score > 21:
        ace = gamer_hand.index(11)
        gamer_hand[ace] = 1
        return gamer_hand

    return gamer_hand


def computer_hand_updater(com_hand, com_score):
    """Force computer to pick another card if computer score is below 17"""

    while com_score < 17:

        print("\n!!Computer picks another card form the deck!!")
        card_dealer(com_hand)
        print(f"Computer\'s hand: {com_hand}")
        com_score = score_calculator(com_hand)
        com_hand = ace_checker(com_hand, com_score)
        com_score = score_calculator(com_hand)

    return com_hand


def pick_winner(side1_score, side2_score):
    """Can judge the game and pick the winner base on score"""

    if side1_score <= 21 < side2_score:
        print("** You Win. **\n")
        return False

    elif side2_score <= 21 < side1_score:
        print("** You Lose! **\n")
        return False

    elif side1_score <= 21 and side2_score <= 21:

        if side1_score > side2_score:
            print("** You Win. **\n")
            return False

        elif side1_score < side2_score:
            print("** You Lose! **\n")
            return False

        else:
            print("** It\'s a Draw. **\n")
            return False

    else:
        print("** It\'s a Draw. **\n")
        return False


def new_game():

    if input("Do you want to play another round?(Y/N) ").lower() == 'y':
        print("\n\n!!New Round!!\n")
        game_engine()

    else:
        print("\nGood Game. See you :)\n")



print(logo)

game_start = input("Hello There!\nDo you want to play some Black Jack?(Y/N) ").lower()

if game_start == 'y':

    # In Black Jack value of J Q and K is 10 and Ace is 11
    card_deck = {
        "Hearths": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        "Spades": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        "Clubs": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        "Diamonds": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    }

    # Call the Game Engine to start the game
    game_engine()

else:
    print("\nOk. See You :)\n")
