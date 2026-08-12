import random

logo = r"""
 ____  _            _    _            _    
| __ )| | __ _  ___| | _(_) __ _  ___| | __
|  _ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\
              ♠ ♥ ♦ ♣  21  ♣ ♦ ♥ ♠
"""

print(logo)

def player():
    player_card = random.choice(cards)
    player_hand.append(player_card)

def computer():
    computer_card = random.choice(cards)
    computer_hand.append(computer_card)

def computer_cards():
    print(f"\nComputer cards were: {computer_hand}")
    print(f"Total of computer cards: [{sum(computer_hand)}]")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

player_hand = []
computer_hand = []

for i in range(0, 2):
        
    player()
    computer()

print(f"Your cards are: {player_hand}")
print(f"Computer card is [{computer_hand[0]}]")
print(f"Total of your cards: [{sum(player_hand)}]")


choice = input("Type Y for another card. N to reveal cards: ").lower()

if choice == "y":
    new_card = "y"
    while new_card == "y":
        player()
        computer()

        print(f"\nYour cards are: {player_hand}")

        player_total = sum(player_hand)
        computer_total = sum(computer_hand)

        print(f"Total of your cards: {sum(player_hand)}")

        if player_total <= 21 and computer_total <= 21:
            new_card = input("Type Y for another card. N to reveal cards: ").lower()

        if new_card == "n":
            if player_total > computer_total and player_total <= 21:
                computer_cards()
                print("You are closer to 21. YOU WIN")
                break
            elif player_total < computer_total and computer_total <= 21:
                computer_cards()
                print("Computer is closer to 21. YOU LOSE")
                break
                
            elif player_total == computer_total and computer_total <= 21:
                computer_cards()
                print("Both are equally close to 21. IT'S A DRAW")
                break
            
        elif player_total > 21 and computer_total <= 21:
            computer_cards()
            print(f"Your total exceeds 21. YOU LOSE")
            new_card = "n"
            break

        elif player_total <= 21 and computer_total > 21:
            computer_cards()
            print(f"Computer total exceeds 21. YOU WIN")
            new_card = "n"
            break

        elif player_total > 21 and computer_total > 21:
            computer_cards()
            if player_total > computer_total:
                print("You exceed 21 by a higher amount. YOU LOSE")
            elif player_total < computer_total:
                print("Computer exceeds 21 by a higher amount. YOU WIN")
            break


else:
    player_total = sum(player_hand)
    computer_total = sum(computer_hand)

    computer_cards()

    if player_total > computer_total and player_total <= 21:
        print("You are closer to 21. YOU WIN")
    elif player_total < computer_total and computer_total <= 21:
        print("Computer is closer to 21. YOU LOSE")
    elif player_total == computer_total and computer_total <= 21:
        print("Both are equally close to 21. IT'S A DRAW")
