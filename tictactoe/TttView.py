import sys
import os


class TttView:

    def __init__(self):
        self.list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.turn = "x"
        self.rounds = 0

    # def play(self):
    #     while self.rounds < 4:
    #         self.rounds = self.rounds + 1
    #         self.draw()
    #         self.placing_chois()

    def draw(self, out=sys.stdout):
        # os.system('clear')
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
        print("befor", self.list)

        self.placing_chois()

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

    def placing_chois(self, out=sys.stdout):
        print("round", self.rounds)
        self.antwood = int(input())
        self.antwood = self.antwood - 1
        self.list[self.antwood] = self.turn
        print("after", self.list)
            # out.write(self.list)
        self.turn_draw()

    def turn_draw(self):
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"
        self.draw()


#         TODO: with python3 -m tictactoe make game loop
#         Todo: game loop
#           Todo: when it is a x or o cant be changed again
#
# antword -1



# if __name__ == '__main__':
#     a = TttView()
#     a.play()

#             list.index("")
#             for
#             string.replace("a", "1")

# for string in strings:
#     new_string = string.replace("a", "1")
#
#     new_strings.append(new_string)


# txt = f" {self.list[n]} | {self.list[n + 1]} | {self.list[n + 2]} "
#
# for string in self.list:
#     self.list = string.replace(self.antwood, self.turn)
