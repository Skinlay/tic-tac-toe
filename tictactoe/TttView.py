import sys


class TttView:

    def __init__(self):
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = "x"

    def draw(self, out=sys.stdout):
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
        n = ln*3
        txt = " {} | {} | {} ".format(self.list[n], self.list[n+1], self.list[n+2])
        return txt

    def which_turn(self, out=sys.stdout):
        if self.turn in ["x", "o"]:
            return self.turn
        else:
            out.write("turn no")
            sys.exit(1)
