import sys
import os
from io import StringIO


class TttView:
    def __init__(self) -> None:
        self.list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.turn = "x"
        self.rounds = 0
        # zet de standaard waarde heel ver buiten de range
        self.antwoord = -100

    def play(self) -> None:
        """Start playing the game."""
        while self.rounds < 10:
            self.rounds = self.rounds + 1
            self.draw(clearscreen=True)
            self.user_input()
            self.placing_choice()
            self.change_drawn_turn()

    def draw(self, out: StringIO = sys.stdout, clearscreen: bool = False) -> None:
        """
        Draw the board on the out variable.
        """
        if clearscreen:
            os.system('clear')

        horizontal_separator = "\n---|---|---\n"
        txt1 = self.drawline(0)
        txt2 = self.drawline(1)
        txt3 = self.drawline(2)

        out.write(txt1)
        out.write(horizontal_separator)
        out.write(txt2)
        out.write(horizontal_separator)
        out.write(txt3)
        out.write("\n")
        out.write("")

    def drawline(self, ln: int) -> str:
        n = ln * 3
        txt = " {} | {} | {} ".format(self.list[n], self.list[n + 1], self.list[n + 2])
        return txt

    def which_turn(self, out: StringIO = sys.stdout) -> str:
        if self.turn in ["x", "o"]:
            return self.turn
        else:
            out.write("turn no")
            sys.exit(1)

    def user_input(self) -> None:
        self.antwoord = int(input()) - 1

    def placing_choice(self) -> None:
        self.list[self.antwoord] = self.turn

    def change_drawn_turn(self) -> None:
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

    #           TODO: with python3 -m tictactoe
    #           TODO: when it is a x or o cant be changed again
    #           TODO: if user inputs 0 9 wil be changed


if __name__ == '__main__':
    a = TttView()
    a.play()


# commentaar waarom niet de wat