import random
from art1 import logo
from replit import clear
import pyautogui




def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Dealer has a Blackjack, You lose."
    elif user_score == 0:
        return "You hava a Blackjack, You win."
    elif user_score > 21:
        return "Your score is over 21, You lose."
    elif computer_score > 21:
        return "Dealer's score is over 21, You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards are {user_cards}, current score is {user_score} ")
        print(f" Computer's first card is {computer_cards[0]} ")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
            #print("You lose. Game over.")


        else:
            ask = input("\nDo you want to draw another card? Type 'y' to get a one otherwise type 'n' to pass. ")
            if ask == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"\n  Your final hand: {user_cards}, final score: {user_score} ")
    print(
        f"  Dealer's final hand: {computer_cards}, final score: {computer_score} "
    )
    print(compare(user_score, computer_score))
   

while input("\nDo you want to play a game of Blackjack? Type 'y' to start the game or type 'n' to go out! ") == "y":
    # clear()
    pyautogui.hotkey('ctrl', 'l')
    game()
