from random import randrange
import tkinter as tk


class GameBoard:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Puzzle")
        self.mw.configure(background="#FBF9F1")
        self.largeur_cell = 30
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
        largeur_cell = 30
        for row in title_row:
            self.canva = tk.Canvas(self.mw, width=30,
                                   height=self.number_square * largeur_cell + 6 * (self.number_square - 1),
                                   background="#FBF9F1")
            self.canva.create_text(5, self.number_square * largeur_cell, text=row, fill="#000", anchor="nw",angle=90)
            self.canva.grid(column=0, rowspan=self.number_square, row=self.start_left)
            self.start_left += self.number_square
            for sub_row in sub_title.get(row):
                self.titles_row.append(sub_row)
                self.canva = tk.Canvas(self.mw, width=200, height=30, background="white")
                label = self.canva.create_text(5, 5, text=sub_row, anchor='nw', fill="black")
                self.canva.grid(column=1, row=self.y_left, rowspan=1)
                self.y_left += 1
        for colum in title_colum:
            self.canva = tk.Canvas(self.mw, height=30,
                                   width=self.number_square * largeur_cell + 6 * (self.number_square - 1),
                                   background="#FBF9F1")
            label = self.canva.create_text(5, 5, text=colum, fill="#000", anchor="nw")
            self.canva.grid(column=self.start_up, columnspan=self.number_square, row=0)
            self.start_up += self.number_square
            for sub_colum in sub_title.get(colum):
                self.titles_colums.append(sub_colum)
                self.canva = tk.Canvas(self.mw, width=largeur_cell, height=200, background="white")
                self.canva.create_text(5, 200, text=sub_colum, angle=90, anchor='nw', fill="black")
                self.canva.grid(column=self.x_up, row=1, columnspan=1)
                self.x_up += 1

    def build_grid(self, title_colum):
        self.pixel = tk.PhotoImage(width=1, height=1)
        for i in range(2, 2 + (self.number_square * len(title_colum))):
            for j in range(2, 2 + (self.number_square * len(title_colum)) - (
                    self.number_square * (int((i - 2) / self.number_square)))):
                self.matrice_text[i - 2][j - 2] = tk.StringVar()
                self.button = tk.Button(self.mw, image=self.pixel, textvariable=self.matrice_text[i - 2][j - 2],
                                        width=30, height=30,
                                        command=lambda row=i, column=j:
                                        self.clicked(row, column), background="#FBF9F1", fg="black", compound='c',
                                        padx=0, pady=0)
                self.button.grid(row=i, column=j, padx=3, pady=3)
                self.matrice_buttons[i - 2][j - 2] = self.button

    def build_constraints(self, liste_constraint):
        i = 0
        for constraint in liste_constraint:
            self.canva = tk.Canvas(self.mw, width=800, height=30, background="#FBF9F1")
            self.canva.create_text(5, 5, text=constraint, fill="#000", anchor="nw")
            self.canva.grid(column=18, row=2 + i)
            i += 1

    def clicked(self, row, column):
        real_row = row - 2
        real_column = column - 2
        if real_row <= 4:
            row_limitMin = 0
            row_limitMax = 5
        elif real_row <= 9:
            row_limitMin = 5
            row_limitMax = 10
        else:
            row_limitMin = 10
            row_limitMax = 15

        if real_column <= 4:
            column_limitMin = 0
            column_limitMax = 5
        elif real_column <= 9:
            column_limitMin = 5
            column_limitMax = 10
        else:
            column_limitMin = 10
            column_limitMax = 15

        # print(real_row, real_column, row_limitMin, row_limitMax, column_limitMin, column_limitMax)

        if self.matrice_text[real_row][real_column].get() == '':
            self.matrice_text[real_row][real_column].set('x')
        elif self.matrice_text[real_row][real_column].get() == 'x':
            # Met 'x' sur la ligne
            for i in range(column_limitMin, column_limitMax):
                mat = self.matrice_text[real_row][i]
                mat_button = self.matrice_buttons[real_row][i]
                if mat is not None:
                    mat.set('x')
                    mat_button["state"] = "disabled"
            # Met 'x' sur la colonne
            for j in range(row_limitMin, row_limitMax):
                mat = self.matrice_text[j][real_column]
                mat_button = self.matrice_buttons[j][real_column]
                if mat is not None:
                    mat.set('x')
                    mat_button["state"] = "disabled"
            self.matrice_text[real_row][real_column].set('o')
            self.matrice_buttons[real_row][real_column]["state"] = "normal"
        else:
            for i in range(column_limitMin, column_limitMax):
                mat = self.matrice_text[real_row][i]
                mat_button = self.matrice_buttons[real_row][i]
                if mat is not None:
                    mat.set('')
                    mat_button["state"] = "normal"
            # Met 'x' sur la colonne
            for j in range(row_limitMin, row_limitMax):
                mat = self.matrice_text[j][real_column]
                mat_button = self.matrice_buttons[j][real_column]
                if mat is not None:
                    mat.set('')
                    mat_button["state"] = "normal"
            self.matrice_text[real_row][real_column].set('')
