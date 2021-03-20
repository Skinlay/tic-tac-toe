import sys


class TttView:
    def draw(self, out=sys.stdout):
        horizontal_separator = "---|---|---\n"
        out.write("   |   |   \n")
        out.write(horizontal_separator)
        out.write("   |   |   \n")
        out.write(horizontal_separator)
        out.write("   |   |   \n")
