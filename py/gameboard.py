from random import randrange
import tkinter as tk


class GameBoard:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Puzzle")
        self.mw.geometry("1700x900")
        self.mw.configure(background="#FBF9F1")
        self.largeur_cell = 25
        self.start_up = 2
        self.start_left = 2
        self.x_up = 2
        self.y_left = 2
        self.number_square = 5
        self.titles_colums = []
        self.titles_row = []
        self.matrice_buttons = [[None for i in range(15)] for j in range(15)]
        self.matrice_text = [[None for i in range(15)] for j in range(15)]

    def build_titles(self, title_row, title_colum, sub_title):
        largeur_cell = 25
        for row in title_row:
            self.canva = tk.Canvas(self.mw, width=25,
                                   height=self.number_square * largeur_cell + 6 * (self.number_square - 1),
                                   background="#FBF9F1")
            label = self.canva.create_text(5, self.number_square * largeur_cell, text=row, fill="#000", anchor="nw",
                                           angle=90)
            self.canva.grid(column=0, rowspan=self.number_square, row=self.start_left)
            self.start_left += self.number_square
            for sub_row in sub_title.get(row):
                self.titles_row.append(sub_row)
                self.canva = tk.Canvas(self.mw, width=200, height=25, background="white")
                label = self.canva.create_text(5, 5, text=sub_row, anchor='nw', fill="black")
                self.canva.grid(column=1, row=self.y_left, rowspan=1)
                self.y_left += 1
        for colum in title_colum:
            self.canva = tk.Canvas(self.mw, height=25,
                                   width=self.number_square * largeur_cell + 6 * (self.number_square - 1),
                                   background="#FBF9F1")
            label = self.canva.create_text(5, 5, text=colum, fill="#000", anchor="nw")
            self.canva.grid(column=self.start_up, columnspan=self.number_square, row=0)
            self.start_up += self.number_square
            for sub_colum in sub_title.get(colum):
                self.titles_colums.append(sub_colum)
                self.canva = tk.Canvas(self.mw, width=largeur_cell, height=200, background="white")
                label = self.canva.create_text(5, 200, text=sub_colum, angle=90, anchor='nw', fill="black")
                self.canva.grid(column=self.x_up, row=1, columnspan=1)
                self.x_up += 1

    def build_grid(self, title_colum):
        self.pixel = tk.PhotoImage(width=1, height=1)
        for i in range(2, 2 + (self.number_square * len(title_colum))):
            for j in range(2, 2 + (self.number_square * len(title_colum)) - (
                    self.number_square * (int((i - 2) / self.number_square)))):
                self.matrice_text[i - 2][j - 2] = tk.StringVar()
                self.button = tk.Button(self.mw, image=self.pixel, textvariable=self.matrice_text[i - 2][j - 2],
                                        width=25, height=25,
                                        command=lambda row=i, column=j:
                                        self.clicked(row, column), background="#FBF9F1", fg="black", compound='c',
                                        padx=0, pady=0)
                self.button.grid(row=i, column=j, padx=3, pady=3)
                self.matrice_buttons[i - 2][j - 2] = self.button

    def build_constraints(self, liste_constraint):
        i = 0
        for constraint in liste_constraint:
            self.canva = tk.Canvas(self.mw, width=800, height=25, background="#FBF9F1")
            label = self.canva.create_text(5, 5, text=constraint, fill="#000", anchor="nw")
            self.canva.grid(column=18, row=2 + i)
            i += 1

    def clicked(self, row, column):
        print(row, column)
        if self.matrice_text[row - 2][column - 2].get() == '':
            self.matrice_text[row - 2][column - 2].set('x')
        elif self.matrice_text[row - 2][column - 2].get() == 'x':
            self.matrice_text[row - 2][column - 2].set('o')
        else:
            self.matrice_text[row - 2][column - 2].set('')
