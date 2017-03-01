from random import randint, choice
import sys
import tkinter

class Bulls_n_cows(object):
    """docstring for bulls_n_cows."""
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.game = game()

    def create_widgets(self):
        self.input = tk.Entry(self)
