import tkinter as tk
from tkinter import ttk

from mzn import Mzn


def on_option_selected(value, index):
    # check_constraint()
    print("nouvel value")


class Interface_Zebre:

    def __init__(self, puzzle):
        self.mw = tk.Tk()
        self.mw.title("Puzzle")
        self.mw.configure(background="#FBF9F1")

        self.options_array = puzzle.get("options_array")
        self.options_left = puzzle.get("options_left")
        self.options_top = puzzle.get("options_top")
        self.constraints = puzzle.get("constraints")
        self.option_menus = []
        self.mat_values = []

        self.puzzle = puzzle

    def create_option_menu(self, frame, options, option_list):
        option_var = tk.StringVar()
        option_menu = ttk.OptionMenu(frame, option_var, *options,
                                 command=lambda event: on_option_selected(option_var, options.index(option_var.get())))
        option_menu.configure(width=10)
        option_var.set(options[0])
        option_list.append(option_var)
        return option_menu

    def build_grid(self):
        option_menus_frame = tk.Frame(self.mw)
        option_menus_frame.pack(padx=0, pady=50)

        # Ajouter des libellés pour chaque colonne
        for i, option_top in enumerate(self.options_top):
            label = tk.Label(option_menus_frame, text=option_top)
            label.grid(row=0, column=i + 1, padx=5, pady=5)

        # Ajouter des libellés pour chaque lignes
        for i, options_left in enumerate(self.options_left):
            label = tk.Label(option_menus_frame, text=options_left)
            label.grid(row=i + 1, column=0, padx=5, pady=5)

        # Ajouter les menus déroulants
        for i, options in enumerate(self.options_array):
            option_list = []
            for j in range(len(self.options_top)):
                option_menu = self.create_option_menu(option_menus_frame, options, option_list)
                option_menu.grid(row=i + 1, column=j + 1, padx=5, pady=5)

                self.option_menus.append([option_menu])
            self.mat_values.append(option_list)

        # Ajouter le bouton
        button = tk.Button(self.mw, text="Check Answer", command=self.buttonClick)
        button.pack()

        # Ajouter les contraintes
        constraint_frame = tk.Frame(self.mw)
        constraint_frame.pack(padx=0, pady=5)
        nbConstraints = len(self.constraints)
        for i, _constraints in enumerate(self.constraints):
            label = tk.Label(constraint_frame, text=_constraints)
            if i >= (nbConstraints / 2):
                label.grid(row=int(i - nbConstraints / 2), column=1, padx=5, pady=5)
            else:
                label.grid(row=i, column=0, padx=5, pady=5)

    def buttonClick(self):
        arrayResult = self.getArrayResults()
        print(self.getArrayresultFromMzn())

    def getArrayResults(self):
        mat_array = []
        for i, list in enumerate(self.mat_values):
            listtemp = []
            for j, values in enumerate(list):
                listtemp.append(values.get())
            mat_array.append(listtemp)
        return mat_array

    def getArrayresultFromMzn(self):
        file = self.puzzle.get("file")
        mzn = Mzn(file)

        mat_array = []
        for solution in mzn.getSolutions():
            mat_array.append(solution.chosenShirts)
            mat_array.append(solution.chosenNames)
            mat_array.append(solution.chosenSurnames)
            mat_array.append(solution.chosenPastas)
            mat_array.append(solution.chosenWhines)
            mat_array.append(solution.chosenAges)
        return mat_array
