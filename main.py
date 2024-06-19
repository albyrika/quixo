from tkinter import Tk, Frame, Button
from itertools import product
from lib.board import Board, button_click


# main window
window = Tk()
window.title("Quixo")

# frame for the buttons
button_frame = Frame(window)
button_frame.pack()

board = Board(button_frame)

# the buttons in a grid
for row, col in product(range(7), range(7)):
    color = "white" if row not in (0, 6) and col not in (0, 6) else "black"

    button = Button(
        button_frame,
        command=lambda r=row, c=col: button_click(r, c, board),
        width=6,
        height=4,
        bg=color,
    )
    button.grid(
        row=row,
        column=col,
        padx=0.1,
        pady=0.1,
    )


window.mainloop()
