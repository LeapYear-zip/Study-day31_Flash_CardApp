import tkinter
import pandas
import random

BG_COLOR = "#B1DDC6"


def learn_word():
    global RAND_FE
    to_learn.remove(RAND_FE)
    print(len(to_learn))
    df = pandas.DataFrame(to_learn)
    df.to_csv("words_to_learn.csv", index=False)
    random_word()


def random_word():
    global RAND_FE
    RAND_FE = random.choice(to_learn)

    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(w_word, text=RAND_FE["French"], fill="black")
    canvas.itemconfig(w_language, text="French", fill="black")
    window.after(ms=3000, func=turn_card)


def turn_card():
    global RAND_FE
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(w_word, text=RAND_FE["English"], fill="white")
    canvas.itemconfig(w_language, text="English", fill="white")


try:
    french_and_english_words = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    french_and_english_words = pandas.read_csv("data/french_words.csv")
to_learn = french_and_english_words.to_dict(orient="records")
RAND_FE = random.choice(to_learn)



# Create Base
window = tkinter.Tk()
window.title("FlashCardAPP")
window.config(padx=50, pady=50, bg=BG_COLOR)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")

canvas = tkinter.Canvas(window, width=800, height=525, bg=BG_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(408, 267, image=card_front)
canvas.grid(row=1, column=1, columnspan=2)

# Create Button
right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=learn_word)
right_button.grid(row=2, column=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=2, column=2)

# random question


# Create text

w_language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
w_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

window.mainloop()
