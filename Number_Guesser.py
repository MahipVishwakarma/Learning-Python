import random

chosen_number = random.randint(1, 100)
difficulty = input("Choose difficulty - Easy (10 tries) or Hard (5 tries): ").lower()

def lower(number):
    if guess < number:
        print("Too low")

def higher(number):
    if guess > number:
        print("Too High")

if difficulty == "easy":
    tries = 10
else:
    tries = 5

while tries > 0:

    guess = int(input("Choose a number between 1 to 100: "))
    tries -= 1

    lower(chosen_number)
    higher(chosen_number)

    print(f"Tries remaining: {tries}")

    if guess == chosen_number:
        print("Congrats you found the number!")
        break

if tries == 0:
    print(f"Unfortunately you couldn't get it. The number was {chosen_number}")