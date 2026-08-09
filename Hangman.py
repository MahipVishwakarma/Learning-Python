import random

stages = [
    """
       ------
       |    |
       |    O
       |   /|\
       |   / \
       |
    --------       
    """,
    """
       ------
       |    |
       |    O
       |   /|\
       |   /
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   
       |   
       |
    --------
    """,
    """
       ------
       |    |
       |   
       |   
       |   
       |
    --------
    """
]

word_list = [
    "python", "guitar", "elephant", "mountain", "rainbow", "keyboard",
    "sandwich", "bicycle", "diamond", "volcano", "butterfly", "chocolate",
    "kangaroo", "telescope", "waterfall", "umbrella", "penguin", "dinosaur",
    "backpack", "hospital", "computer", "airplane", "notebook", "sunflower",
    "hurricane", "lighthouse", "chessboard", "octopus", "campfire", "jacket"
]
# chooses random word
chosen_word = random.choice(word_list)  
print(chosen_word)

# starts the blanks
placeholder = ""  

for postion in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

# Must initiate this variable so that while loop is not infinite 
game_over = False

# Must initiate this list so that the letters you guessed correctly are saved
correct_letter = []

lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    # Main thing is this. We start the empty string (display) so that we can actually start the guessing.
    for letter in chosen_word:
        if guess == letter:     #This will replace the _ with the correct letter
            display += letter
            correct_letter.append(letter)

        elif letter in correct_letter: # This will help you save the etter you guessed previously
            display += letter
            
        else:
            display += "_"

    if guess not in chosen_word: # Everything after this is self explainatory
        lives -= 1
        if lives == 0:
            game_over = True
            print("You LOSE")
    
    print(display)
    print(f"Lives left {lives}")
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You WIN!")