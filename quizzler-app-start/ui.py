from tkinter import *


THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self):

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label("Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=3, row=0)





        self.window.mainloop()