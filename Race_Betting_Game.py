from turtle import Turtle, Screen
import random

race_is_on = False

screen = Screen()
screen.setup(600, 500)
user_bet = screen.textinput("Make Your Guess", "Choose the colour of your turtle: ").lower()

race_is_on = True

colour = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_coord = 90

if user_bet not in colour:
    print(f"There was no bet. The user is here to enjoy the game!")
    user_bet = ""
else:
    print(f"User is rooting for the {user_bet} turtle.")



for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colour[i])
    tim.goto(-280, (y_coord))
    y_coord -= 30
    turtles.append(tim)

while race_is_on:

    for i in turtles:
        steps = random.randint(0,10)
        i.forward(steps)

        if i.xcor() > 300:
            winner = i.pencolor()
            race_is_on = False
            if user_bet == winner:
                print(f"You win! The {winner} turtle was the winner.")
            elif user_bet == "":
                print(f"The {winner} turtle was the winner!!")
            else:
                print(f"You lose! The {winner} turtle was the winner.")

screen.exitonclick()