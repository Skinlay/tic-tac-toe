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

    def placing_chois(self):
        print("round", self.rounds)
        self.antwood = input()
        for string in self.list:
            self.list = string.replace(self.antwood, self.turn)
            print(self.list)

        self.draw()

#         TODO: with python3 -m tictactoe make game loop
#
#         TODO: when second time through loop:
#                   File "/home/caitlin/Projecten/tic-tac-toe/tictactoe/TttView.py", line 38, in drawline
#                       txt = " {} | {} | {} ".format(self.list[n], self.list[n + 1], self.list[n + 2])
#                   IndexError: string index out of range



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
