from tkinter import Tk, Frame, Button
from itertools import product


class Board:
    def __init__(self, button_frame) -> None:
        self.button_frame = button_frame
        self.selected_position: tuple[int, int] = (-1, -1)
        self.previous_position: tuple[int, int] = (-1, -1)
        self.turn: int = 0

    def __move(self) -> None:
        # TODO: implement
        self.turn = (self.turn + 1) % 2

    def select_piece(self, row, col):
        border = row in (0, 6) or col in (0, 6)
        if not border:
            button = Button(
                self.button_frame,
                command=lambda r=row, c=col: button_click(r, c, self),
                width=6,
                height=4,
                bg="blue" if self.turn == 0 else "red",
            )
            button.grid(row=row, column=col, padx=0.1, pady=0.1)
            self.__move()

    def reset_board(self):
        for row, col in product(range(7), range(7)):
            color = "white" if row not in (0, 6) and col not in (0, 6) else "black"
            button = Button(
                button_frame,
                text="(X)" if color == "white" else "",
                command=lambda r=row, c=col: button_click(r, c),
                width=6,
                height=4,
                bg=color,
            )
            button.grid(row=row, column=col, padx=0.1, pady=0.1)


def button_click(row, col, board: Board):
    # TODO: add here all the logic, through Manager
    board.select_piece(row, col)


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
