from random import randrange
import tkinter as tk

from py.mzn import Mzn


class GameBoard:

    def __init__(self, puzzle):
        self.mw = tk.Tk()
        self.mw.title("Puzzle")
        self.mw.configure(background="#FBF9F1")
        self.largeur_cell = 30
        self.start_up = 2
        self.start_left = 2
        self.x_up = 2
        self.y_left = 2
        self.number_square = 5
        self.reponse_matrice = [[None for i in range(4)] for j in range(self.number_square)]
        self.titles_colums = []
        self.titles_row = []
        self.matrice_buttons = [[None for i in range(15)] for j in range(15)]
        self.matrice_text = [[None for i in range(15)] for j in range(15)]

        self.puzzle = puzzle

    def build_titles(self, title_row, title_colum, sub_title):
        largeur_cell = 30
        acc = 0
        for i in self.reponse_matrice:
            if(title_row[0]=="Monitor"):
                i[0] = sub_title.get(title_row[0])[acc][:-1]
            else:
                i[0] = sub_title.get(title_row[0])[acc]
            acc += 1
        for row in title_row:
            self.canva = tk.Canvas(self.mw, width=30,
                                   height=self.number_square * largeur_cell + 6 * (self.number_square - 1),
                                   background="#FBF9F1")
            self.canva.create_text(5, self.number_square * largeur_cell, text=row, fill="#000", anchor="nw", angle=90)
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
            nbline = constraint.count("\n")
            self.canva = tk.Canvas(self.mw, width=800, height=35 + 20 * nbline, background="#FBF9F1")
            self.canva.create_text(5, 5, text=constraint, fill="#000", anchor="nw")
            self.canva.grid(column=18, row=2 + i, rowspan=1 + nbline)
            i += 1 + nbline
        self.button = tk.Button(self.mw, image=self.pixel,
                                width=400, height=35,
                                command=lambda: self.ButtonCheckAnswer(), background="#FBF9F1", fg="black",
                                text="Tester", compound='c',
                                padx=0, pady=0)
        self.button.grid(row=2 + i, column=18, padx=3, pady=3)

    def popUp(self, title, text):
        top = tk.Toplevel(self.mw)
        top.geometry("350x250")
        top.title(title)
        tk.Label(top, text=text, font=('Mistral 18 bold')).place(x=150, y=80)

    def getArrayResultFromMnz(self):
        file = self.puzzle.get("file")
        solution = Mzn(file).getSolutions().solution

        if self.puzzle.get("name") == "Computers":
            temp = [solution.chosenMonitors, solution.chosenProcessors, solution.chosenHDs, solution.chosenPrices]
            mat_response = [[0 for j in range(len(temp))] for i in range(len(temp[0]))]
            for i, tmp in enumerate(temp):
                for j in range(len(tmp)):
                    if i == 0 or i == 1:
                        mat_response[j][i] = str(tmp[j] / 10)
                    else:
                        mat_response[j][i] = str(tmp[j])
                    if i == 0 and ".0" in mat_response[j][i]:
                        mat_response[j][i] = str(int(tmp[j] / 10))

        elif self.puzzle.get("name") == "Alpacino":
            temp = [solution.ChosenNames, solution.ChosenFilm, solution.ChosenDay, solution.ChosenTime]
            mat_response = [[0 for j in range(len(temp))] for i in range(len(temp[0]))]
            for i, tmp in enumerate(temp):
                for j in range(len(tmp)):
                    mat_response[j][i] = tmp[j]
        return mat_response

    def ButtonCheckAnswer(self):
        mznResult = self.getArrayResultFromMnz()

        for i, value in enumerate(mznResult):
            if value not in self.reponse_matrice:
                self.popUp("You loose!", "Nope!")
                return

        self.popUp("You win!", "Good job!")

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
            if self.puzzle.get("name") == "Computers":
                if (real_column // self.number_square == 0):
                    formatted_reponse = self.titles_colums[real_column][:-4]
                elif (real_column // self.number_square == 1):
                    formatted_reponse = self.titles_colums[real_column][:-3]
                elif (real_column // self.number_square == 2):
                    formatted_reponse = self.titles_colums[real_column][2:-3].replace(".", "")
            else:
                if(real_column//self.number_square==2):
                    formatted_reponse=(int(self.titles_colums[real_column].split(":")[0])+12)*60+int(self.titles_colums[real_column].split(":")[1])
                else:
                    if(self.titles_colums[real_column]=="88 Minutes"):
                        formatted_reponse="eighty_eight_Minutes"
                    else:
                        formatted_reponse=self.titles_colums[real_column].replace(" ","_")
                self.reponse_matrice[real_row][1+real_column//self.number_square]=formatted_reponse
            self.reponse_matrice[real_row][1 + real_column // self.number_square] = formatted_reponse

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
