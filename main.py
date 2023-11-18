from tkinter import *
import pandas
import random
import time


try:
    french_words_data = pandas.read_csv("data/cards_to_learn.csv")
except FileNotFoundError:
    french_words_data = pandas.read_csv("data/french_words.csv")
    french_words_table = pandas.DataFrame(french_words_data)
    french_words_table.to_csv("cards_to_learn.csv")
    french_words_dict = french_words_table.to_dict(orient="records")
    current_word_pair = {}
else:
    french_words_table = pandas.DataFrame(french_words_data)
    french_words_table.to_csv("cards_to_learn.csv")
    french_words_dict = french_words_table.to_dict(orient="records")
    current_word_pair = {}


def know_card():
    french_words_dict.remove(current_word_pair)
    learning_data = pandas.DataFrame(french_words_dict)
    learning_data.to_csv("data/cards_to_learn.csv", index=False)
    change_card()



def change_card():
    global current_word_pair, delay
    window.after_cancel(delay)
    random_word_pair = random.choice(french_words_dict)
    new_french_word = random_word_pair["french"]
    current_word_pair = random_word_pair
    canvas.itemconfig(word_text, text=new_french_word, fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    delay = window.after(3000, flip_card)


def flip_card():
    global current_word_pair
    english_translation = current_word_pair["english"]
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_translation, fill="white")

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
correct_img = PhotoImage(file="images/right.png")
incorrect_img = PhotoImage(file="images/wrong.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)





# Buttons
correct_button = Button(image=correct_img, highlightthickness=0, command=know_card)
correct_button.grid(column=0, row=1)

incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=change_card)
incorrect_button.grid(column=1, row=1)


delay = "Just needed this to be global"
change_card()
window.mainloop()