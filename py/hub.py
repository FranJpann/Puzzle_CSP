import tkinter as tk

from interface_zebre import Interface_Zebre
from py.gameboard import GameBoard
from py.vars import *


class Hub:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Hub")
        self.mw.configure(background="#FBF9F1")

        button1 = tk.Button(self.mw, text='Puzzle Alpachino', command=self.on_click_alpachino)
        button1.pack()
        button2 = tk.Button(self.mw, text='Puzzle Computers', command=self.on_click_computers)
        button2.pack()
        button3 = tk.Button(self.mw, text='Puzzle Pasta and wine', command=self.on_click_pastawine)
        button3.pack()

    def on_click_alpachino(self):
        self.launch_gameboard("Alpachino")

    def on_click_computers(self):
        self.launch_gameboard("Computers")

    def on_click_pastawine(self):
        self.launch_zebre(Pastawine)

    def launch_gameboard(self, puzzle):
        self.mw.destroy()
        gboard = GameBoard()
        gboard.build_titles(Rows.get(puzzle), Columns.get(puzzle), Data)
        gboard.build_grid(Columns.get(puzzle))
        gboard.build_constraints(Constraints.get(puzzle))

    def launch_zebre(self, puzzle):
        self.mw.destroy()
        interface_zebre = Interface_Zebre(puzzle)
        interface_zebre.build_grid()
