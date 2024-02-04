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
        self.launch_gameboard(Alpachino)

    def on_click_computers(self):
        self.launch_gameboard(Computers)

    def on_click_pastawine(self):
        self.launch_zebre(Pastawine)

    def launch_gameboard(self, puzzle):
        self.mw.destroy()
        gboard = GameBoard(puzzle)
        gboard.build_titles(puzzle.get("Rows"), puzzle.get("Columns"), puzzle.get("Data"))
        gboard.build_grid(puzzle.get("Columns"))
        gboard.build_constraints(puzzle.get("Constraints"))

    def launch_zebre(self, puzzle):
        self.mw.destroy()
        interface_zebre = Interface_Zebre(puzzle)
        interface_zebre.build_grid()
