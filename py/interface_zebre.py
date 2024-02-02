from random import randrange
import tkinter as tk
from tkinter import ttk


def on_option_selected(value, index):
    print("ouais")


def create_option_menu(frame, options):
    option_var = tk.StringVar()
    option_menu = ttk.OptionMenu(frame, option_var, *options,
                                 command=lambda event: on_option_selected(option_var, options.index(option_var.get())))
    option_var.set(options[0])
    return option_menu


class Interface_Zebre:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Puzzle")
        self.mw.geometry("1700x900")
        self.mw.configure(background="#FBF9F1")

    def build_grid(self):
        option_menus_frame = tk.Frame(self.mw)
        option_menus_frame.pack(padx=10, pady=10)
        option_menus = []

        for i, options in enumerate(options_pastawine):
            for j in range(number_column):
                option_menu = create_option_menu(option_menus_frame, options)
                option_menu.grid(row=i, column=j, padx=5, pady=5)
                option_menus.append(option_menu)

    def clicked(self):
        print("ouais")


options_pastawine = [
    ["red", "blue", "green", "white", "yellow"],
    ["Holly", "Andrea", "Julie", "Leslie", "Victoria"],
    ["Davis", "Wilson", "Miller", "Lopes", "Brown"],
    ["farfalle", "lasagne", "penne", "spaghetti", "ravioli"],
    ["Italian", "French", "Chilean", "Argentine", "Australian"],
    ["30 years", "35 years", "40 years", "45 years", "50 years"]
]

number_column = 5
