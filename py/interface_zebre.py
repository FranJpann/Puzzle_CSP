from random import randrange
import tkinter as tk
from tkinter import ttk


def on_option_selected(value, index):
    check_constraint()


def create_option_menu(frame, options):
    option_var = tk.StringVar()
    option_menu = ttk.OptionMenu(frame, option_var, *options,
                                 command=lambda event: on_option_selected(option_var, options.index(option_var.get())))
    option_menu.configure(width=10)
    option_var.set(options[0])
    return option_menu


class Interface_Zebre:

    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Puzzle")
        self.mw.configure(background="#FBF9F1")

        self.option_menus = []

    def build_grid(self, puzzle):
        option_menus_frame = tk.Frame(self.mw)
        option_menus_frame.pack(padx=0, pady=100)

        options_array = puzzle.get("options_array")
        options_left = puzzle.get("options_left")
        options_top = puzzle.get("options_top")

        # Ajouter des libellés pour chaque colonne
        for i, option_top in enumerate(options_top):
            label = tk.Label(option_menus_frame, text=option_top)
            label.grid(row=0, column=i + 1, padx=5, pady=5)

        # Ajouter des libellés pour chaque lignes
        for i, options_left in enumerate(options_left):
            label = tk.Label(option_menus_frame, text=options_left)
            label.grid(row=i + 1, column=0, padx=5, pady=5)

        # Ajouter les menus déroulants
        for i, options in enumerate(options_array):
            for j in range(len(options_top)):
                option_menu = create_option_menu(option_menus_frame, options)
                option_menu.grid(row=i + 1, column=j + 1, padx=5, pady=5)

                self.option_menus.append([option_menu])

        # Ajouter les contraintes
        constraint_frame = tk.Frame(self.mw)
        constraint_frame.pack(padx=0, pady=5)
        constraints = puzzle.get("constraints")
        nbConstraints = len(constraints)
        for i, _constraints in enumerate(constraints):
            label = tk.Label(constraint_frame, text=_constraints)
            if i >= (nbConstraints / 2): label.grid(row=int(i - nbConstraints / 2), column=1, padx=5, pady=5)
            else: label.grid(row=i, column=0, padx=5, pady=5)

    def clicked(self):
        print("ouais")
