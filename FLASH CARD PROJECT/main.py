from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#------------------------------------------------------------------------------------
def reset_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=front_img)
    canvas.itemconfig(title, text="French", fill="black")
    count_down()

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    reset_word()

def flip_card():
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")

def count_down():

    global timer
    timer = window.after(3000, flip_card)

#------------------------------------------------------------------------------------

try:
    data1 = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data1.to_dict(orient="records")

current_card = {}

#------------------------------------------------------------------------------------

window = Tk()
window.title("Flash Card Project")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="C:/Users/admin/Python Projects/FLASH CARD PROJECT/images/card_back.png")
front_img = PhotoImage(file="C:/Users/admin/Python Projects/FLASH CARD PROJECT/images/card_front.png")
card = canvas.create_image(410, 281, image=front_img)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Click the Red Button", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="C:/Users/admin/Python Projects/FLASH CARD PROJECT/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="C:/Users/admin/Python Projects/FLASH CARD PROJECT/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=reset_word)
wrong_button.grid(column=1, row=1)

timer = window.after(3000, flip_card)
reset_word()

window.mainloop()

window.mainloop()