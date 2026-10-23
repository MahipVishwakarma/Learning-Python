import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

correct_guesses = []
game_is_on = True

while game_is_on:

    answer_state = screen.textinput(f"{score}/50 States Guessed", "What state do you wanna check?").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].to_list()
    
    if answer_state in all_states and answer_state not in correct_guesses:
        score += 1
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
                
    

turtle.mainloop()