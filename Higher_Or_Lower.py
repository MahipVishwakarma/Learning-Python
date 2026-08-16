import random

CELEBRITIES = [
    {"name": "Cristiano Ronaldo", "followers": 650, "profession": "Footballer", "nationality": "Portuguese"},
    {"name": "Lionel Messi", "followers": 500, "profession": "Footballer", "nationality": "Argentine"},
    {"name": "Selena Gomez", "followers": 420, "profession": "Singer/Actress", "nationality": "American"},
    {"name": "Kylie Jenner", "followers": 400, "profession": "Media Personality", "nationality": "American"},
    {"name": "Dwayne Johnson", "followers": 395, "profession": "Actor", "nationality": "American"},
    {"name": "Ariana Grande", "followers": 380, "profession": "Singer", "nationality": "American"},
    {"name": "Kim Kardashian", "followers": 360, "profession": "Media Personality", "nationality": "American"},
    {"name": "Beyoncé", "followers": 320, "profession": "Singer", "nationality": "American"},
    {"name": "Khloé Kardashian", "followers": 310, "profession": "Media Personality", "nationality": "American"},
    {"name": "Justin Bieber", "followers": 295, "profession": "Singer", "nationality": "Canadian"},
    {"name": "Kendall Jenner", "followers": 290, "profession": "Model", "nationality": "American"},
    {"name": "Taylor Swift", "followers": 280, "profession": "Singer", "nationality": "American"},
    {"name": "Virat Kohli", "followers": 270, "profession": "Cricketer", "nationality": "Indian"},
    {"name": "Jennifer Lopez", "followers": 250, "profession": "Singer/Actress", "nationality": "American"},
    {"name": "Nicki Minaj", "followers": 230, "profession": "Rapper", "nationality": "American"},
    {"name": "Neymar Jr", "followers": 225, "profession": "Footballer", "nationality": "Brazilian"},
    {"name": "Miley Cyrus", "followers": 215, "profession": "Singer", "nationality": "American"},
    {"name": "Katy Perry", "followers": 210, "profession": "Singer", "nationality": "American"},
    {"name": "Kevin Hart", "followers": 205, "profession": "Comedian/Actor", "nationality": "American"},
    {"name": "Zendaya", "followers": 185, "profession": "Actress", "nationality": "American"},
    {"name": "Cardi B", "followers": 165, "profession": "Rapper", "nationality": "American"},
    {"name": "Rihanna", "followers": 155, "profession": "Singer", "nationality": "Barbadian"},
    {"name": "Chris Brown", "followers": 145, "profession": "Singer", "nationality": "American"},
    {"name": "Demi Lovato", "followers": 145, "profession": "Singer/Actress", "nationality": "American"},
    {"name": "Kylian Mbappé", "followers": 130, "profession": "Footballer", "nationality": "French"},
    {"name": "Billie Eilish", "followers": 120, "profession": "Singer", "nationality": "American"},
    {"name": "Vin Diesel", "followers": 105, "profession": "Actor", "nationality": "American"},
    {"name": "Priyanka Chopra", "followers": 95, "profession": "Actress", "nationality": "Indian"},
    {"name": "Shakira", "followers": 90, "profession": "Singer", "nationality": "Colombian"},
    {"name": "Emma Watson", "followers": 80, "profession": "Actress", "nationality": "British"},
]

def celebrity():
    chosen_celebrity = random.choice(CELEBRITIES)
    chosen_name, chosen_followers, chosen_profession, chosen_nationality = chosen_celebrity['name'], chosen_celebrity['followers'], chosen_celebrity['profession'], chosen_celebrity['nationality']
    return chosen_name, chosen_followers, chosen_profession, chosen_nationality

LOGO = """
╔═══════════════════════════════════╗
║    H I G H E R  or  L O W E R  🎮 ║
║   Celebrity Instagram Followers   ║
╚═══════════════════════════════════╝
"""

print(LOGO)

A_name, A_followers, A_profession, A_nationality = celebrity()
print(f"Person A is {A_name}, whose nationality is {A_nationality} and is a professional {A_profession}")

B_name, B_followers, B_profession, B_nationality = celebrity()
print(f"Person B is {B_name}, whose nationality is {B_nationality} and is a professional {B_profession}")

points = 0
game_over = False

while not game_over:

    guess = input("Who do you think has more followers on instagram (A or B): ").lower()

    if guess != "a" and "b":
        print("\nYou had to choose from either A or B. GAME OVER")
        break

    if A_followers == B_followers:
        print("\nIt's a tie! Free pass, moving on.")

    elif guess == "a" and A_followers > B_followers:
        print("\nYou are correct! +1 point for you")
        points += 1
        print(f"You have {points} points")

    elif guess == "b" and A_followers > B_followers:
        print("\nYou were wrong. You Lose :(")
        game_over = True
        print(f"You had {points} points")
        break

    elif guess == "a" and A_followers < B_followers:
        print("\nYou were wrong. You Lose :(")
        game_over = True
        print(f"You had {points} points")
        break

    elif guess == "b" and A_followers < B_followers:
        print("\nYou are correct! +1 point for you")
        points += 1
        print(f"You have {points} points")

    print("\n" * 2)

    A_name, A_followers, A_profession, A_nationality = B_name, B_followers, B_profession, B_nationality
    print(f"Person A is {A_name}, whose nationality is {A_nationality} and is a professional {A_profession}")

    B_name, B_followers, B_profession, B_nationality = celebrity()
    print(f"Person B is {B_name}, whose nationality is {B_nationality} and is a professional {B_profession}")
