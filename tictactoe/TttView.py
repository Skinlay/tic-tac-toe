import sys
import os


class TttView:

    def __init__(self):
        self.list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.turn = "x"
        self.rounds = 0
        self.antwoord = -1

    def play(self):
        while self.rounds < 4:
            self.rounds = self.rounds + 1
            self.draw()
            self.user_input()
            self.placing_choice()
            self.change_drawn_turn()

    def draw(self, out=sys.stdout):
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

    def drawline(self, ln):
        n = ln * 3
        txt = " {} | {} | {} ".format(self.list[n], self.list[n + 1], self.list[n + 2])
        return txt

    def which_turn(self, out=sys.stdout):
        if self.turn in ["x", "o"]:
            return self.turn
        else:
            out.write("turn no")
            sys.exit(1)

    def user_input(self):
        self.antwoord = int(input()) - 1

    def placing_choice(self, out=sys.stdout):
        print("round", self.rounds)
        self.list[self.antwoord] = self.turn
        out.write(str(self.list))

    #     if user inputs 0 9 wil be changed

    def change_drawn_turn(self):
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

    #         TODO: with python3 -m tictactoe
    #         Todo: game loop
    #           Todo: when it is a x or o cant be changed again


if __name__ == '__main__':
    a = TttView()
    a.play()
