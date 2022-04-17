from string import whitespace
from struct import pack
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import filedialog as fd
from tkinter import *
from tkinter.ttk import *


# List with a full game
GameList = [
    "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR",
    "rnbqkbnrppppppp.p.................................PPPPPPPPRNBQKBNR",
    "rnbqkbnrppppppp.p...............................P..PPPPPPPRNBQKBNR",
]


# Also will return a list with games for the users to select after sending file to open
GamesInFileList = [
    "Game 1 - Player Makis - Player 2 Thanasis",
    " Game 2 - Player 1 Thanasis - Player 2 Nikos",
]


# Also will return a list with games for the users to select after sending file to open


# class for building and managing the game board
class GameBoard:
    def __init__(self, appwindow, width, height):

        self.width = width
        self.height = height

        self.canvas = tk.Canvas(
            appwindow,
            borderwidth=0,
            highlightthickness=0,
            width=self.width * 2,
            height=self.height,
            background="bisque",
        )
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.images = []

        # Build the board
        color1 = "white"
        color2 = "grey"
        color = color1
        offsetx = 20  # Where to start drawing of the board in x axis
        offsety = 20  # Where to start drawing of the board in y axis
        square_size = 70
        for row in range(0, 8):
            color = color1 if color == color2 else color2
            for col in range(0, 8):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="black", fill=color, tags="square"
                )
                color = color1 if color == color2 else color2

        # test to place a pawn
        self.images = []
        for i in range(0, 64):
            r = int(i // 8)
            c = int(i - r * 8)
            self.placepiece(
                r, c, square_size, GameList[0][i]
            )  # Place piece in coordinates, square_size, piece type  first number = row, second = col starts at 0

            # Maybe it is best to create a list with objects the images created for every piece.
            # Then place the pieces.
            # When need to redray distroy every image and create them again for the new board.

    def placepiece(self, row, col, square_size, piece):
        x = (col * square_size) + int(square_size / 2)
        y = (row * square_size) + int(square_size / 2)

        image_to_place = None
        if piece == "p":
            image_to_place = tk.PhotoImage(file="icons/b_pawn.png")
            # self.canvas.create_image(x,y, image=self.image_to_place_p, tags="piece" ,anchor="c")
        elif piece == "r":
            image_to_place = tk.PhotoImage(file="icons/b_rook.png")
        elif piece == "n":
            image_to_place = tk.PhotoImage(file="icons/b_knight.png")
        elif piece == "b":
            image_to_place = tk.PhotoImage(file="icons/b_bishop.png")
        elif piece == "q":
            image_to_place = tk.PhotoImage(file="icons/b_queen.png")
        elif piece == "k":
            image_to_place = tk.PhotoImage(file="icons/b_king.png")
        elif piece == "P":
            image_to_place = tk.PhotoImage(file="icons/w_pawn.png")
        elif piece == "R":
            image_to_place = tk.PhotoImage(file="icons/w_rook.png")
        elif piece == "N":
            image_to_place = tk.PhotoImage(file="icons/w_knight.png")
        elif piece == "B":
            image_to_place = tk.PhotoImage(file="icons/w_bishop.png")
        elif piece == "Q":
            image_to_place = tk.PhotoImage(file="icons/w_queen.png")
        elif piece == "K":
            image_to_place = tk.PhotoImage(file="icons/w_king.png")
        self.images.append(image_to_place)

        if piece != ".":
            self.canvas.create_image(
                x, y, image=image_to_place, tags="piece", anchor="c"
            )
            self.canvas.update


# class for building and managing the application windows
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("PLH PRO CHESS")
        self.geometry("1000x565")
        self.resizable("false", "false")
        self.create_menu()
        self.board = GameBoard(self, 500, 500)

    def create_menu(self):
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar)
        self.file_menu = Menu(self.menubar, tearoff=False)

        self.file_menu.add_command(label="Open", command=self.select_file)
        self.file_menu.add_command(label="Exit", command=self.destroy)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def select_file(self):
        """Open a select file dialogbox and returns the name of the file"""
        filetypes = (("PGN files", "*.pgn"), ("All files", "*.*"))
        filename = fd.askopenfilename(
            title="Open a PGN file...", initialdir="/", filetypes=filetypes
        )
        showinfo(title="Selected File", message=filename)
        sgw = select_game_window(self)  # Create select game window
        # sgw.grab_set() # The user can't select the main windows if he has not closed the select game window first


# created a select game window for the user to select the game
class select_game_window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("500x300+500+500")
        self.title("Select Game...")
        self.resizable("false", "false")

        self.label1 = Label(
            self, text="Please select a game from the list:", width=100
        ).place(x=5, y=5)

        games_var = StringVar(
            value=GamesInFileList
        )  # The list with the games in the file
        self.listbox = Listbox(
            self, listvariable=games_var, selectmode="browse", height=10, width=80
        ).place(x=5, y=25)

        self.closebtn = ttk.Button(self, text="Close", command=self.destroy).place(
            x=5, y=200
        )
        self.selectbtn = ttk.Button(
            self, text="Select", command=self.select_game_button
        ).place(x=100, y=200)

    def select_game_button(self):
        showinfo(title="Selected Game", message="test message")
        self.destroy


if __name__ == "__main__":
    app = App()
    app.mainloop()
