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
        self.xAntwoordList = []
        self.oAntwoordList = []
        self.test = (3, 4, 5)

    def play(self) -> None:
        """Start playing the game."""
        while self.rounds < 10:
            self.rounds = self.rounds + 1
            # needs to be on False for testing
            self.draw(clearscreen=True)
            foo = False
            while not foo:
                foo = self.user_input()
            self.player_won
            self.placing_choice()
            self.change_drawn_turn()

    def draw(self, out: StringIO = sys.stdout, clearscreen: bool = False) -> None:
        """
        Draw the board on the out variable.
        """
        # if clearscreen:
        #     os.system('clear')

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

    def user_input(self, out: StringIO = sys.stdout, print_error: bool = True) -> bool:
        # get user input and substrexts 1 so it is gelijk met de lijst
        self.antwoord = int(input()) - 1
        # checks if user input is in range
        # if this is not check the user can give numbers like 0 or -1
        if self.antwoord not in range(0, 9):
            if print_error:
                print("that is not in range of 1-9")
            return False
        else:
            # TODO: Make one if
            # checks if given answer hasn't already bin given
            if self.antwoord in self.xAntwoordList:
                if print_error:
                    print("is already in use")
                return False
            elif self.antwoord in self.oAntwoordList:
                if print_error:
                    print("is already in use")
                return False
            # saves given answer in correct list of the payer
            else:
                if self.turn == "x":
                    self.xAntwoordList.append(self.antwoord)
                    print(self.xAntwoordList, self.oAntwoordList)
                    return True
                else:
                    self.oAntwoordList.append(self.antwoord)
                    print(self.xAntwoordList, self.oAntwoordList)
                    return True

    def placing_choice(self) -> None:
        # in list change the given answer into the current turn (x or o)
        # this wil change the list and it wil be drawn onto the bord next loop
        self.list[self.antwoord] = self.turn


    # TODO: check if numbers are in the list
    @property
    def player_won(self) -> None:
        if self.turn == "x":
            if all(self.test) in self.xAntwoordList:
                print("congratulations")
                return True
        else:
            print("PANIEK")
            return True

    #if 0 in self.xAntwoordList:
    #if all(self.test) in self.xAntwoordList:

# if any(s in line for s in ('string1', 'string2', ...)):
# all([predicate(item) for item in iterable])


    def change_drawn_turn(self) -> None:
        # changing turn so you now who placed
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

    def occupied(self) -> None:
        pass

    #           TODO: ~/PycharmProjects/tic-tac-toe
    #           TODO: with python3 -m tictactoe

    #           TODO: if a win


if __name__ == '__main__':
    a = TttView()
    a.play()

# commentaar waarom, niet de wat

# if y == [1]:
