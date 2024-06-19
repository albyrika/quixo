from tkinter import Tk, Frame, Button
from itertools import product


def button_click(row, col, board):
    board.select_piece(row, col)


class Board:
    def __init__(self, button_frame: Frame) -> None:
        self.button_frame = button_frame
        self.selected_position: tuple[int, int] = (-1, -1)
        self.previous_position: tuple[int, int] = (-1, -1)
        self.turn: int = 0

    def __move(self) -> None:
        # TODO: implement
        self.turn = (self.turn + 1) % 2

    def __reset_border(self) -> None:
        # TODO: optimize
        for row, col in product(range(7), range(7)):
            outer = row in (0, 6) or col in (0, 6)
            if not outer:
                continue
            button = Button(
                self.button_frame,
                command=lambda r=row, c=col: button_click(r, c, self),
                width=6,
                height=4,
                bg="black",
            )
            button.grid(row=row, column=col, padx=0.1, pady=0.1)

    def __illuminate_border(self, row, col):
        self.__reset_border()
        case_coords: list[tuple[int, int]] = []
        for new_col in [0, 6]:
            case_coords += (
                []
                if (col == 1 and new_col == 0) or (col == 5 and new_col == 6)
                else [(row, new_col)]
            )
        for new_row in [0, 6]:
            case_coords += (
                []
                if (row == 1 and new_row == 0) or (row == 5 and new_row == 6)
                else [(new_row, col)]
            )

        for coords in case_coords:
            sign = "➡️"
            if coords[0] == 0:
                sign = "⬇️"
            if coords[0] == 6:
                sign = "⬆️"
            if coords[1] == 6:
                sign = "⬅️"
            button = Button(
                self.button_frame,
                command=lambda r=coords[0], c=coords[1]: button_click(r, c, self),
                width=6,
                height=4,
                bg="grey",
                text=sign,
            )
            button.grid(row=coords[0], column=coords[1], padx=0.1, pady=0.1)

    def select_piece(self, row, col):
        outer = row in (0, 6) or col in (0, 6)
        border = not outer and (row in (1, 5) or col in (1, 5))
        if border:
            button = Button(
                self.button_frame,
                command=lambda r=row, c=col: button_click(r, c, self),
                width=6,
                height=4,
                bg="blue" if self.turn == 0 else "red",
            )
            button.grid(row=row, column=col, padx=0.1, pady=0.1)
            self.__move()  # change turns
            self.__illuminate_border(row, col)  # modify border pieces

    def reset_board(self):
        for row, col in product(range(7), range(7)):
            color = "white" if row not in (0, 6) and col not in (0, 6) else "black"
            button = Button(
                self.button_frame,
                text="(X)" if color == "white" else "",
                command=lambda r=row, c=col: button_click(r, c, self),
                width=6,
                height=4,
                bg=color,
            )
            button.grid(row=row, column=col, padx=0.1, pady=0.1)
