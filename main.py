from tkinter import Tk, Frame, Button
from itertools import product


class Board:
    def __init__(self) -> None:
        self.selected_position: tuple[int, int] = (-1, -1)
        self.previous_position: tuple[int, int] = (-1, -1)

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


def button_click(row, col):
    # TODO: add here all the logic, through Manager
    button = Button(
        button_frame,
        text="(X)",
        width=6,
        height=4,
        bg="yellow",
    )
    button.grid(row=row, column=col, padx=0.1, pady=0.1)


# main window
window = Tk()
window.title("Quixo")

# frame for the buttons
button_frame = Frame(window)
button_frame.pack()

# the buttons in a grid
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
    button.grid(
        row=row,
        column=col,
        padx=0.1,
        pady=0.1,
    )


window.mainloop()
