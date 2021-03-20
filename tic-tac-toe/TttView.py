import sys


class TttView:
    def draw(self, out=sys.stdout):
        out.write("   |   |   \n")
        out.write("---|---|---\n")
        out.write("   |   |   \n")
        out.write("---|---|---\n")
        out.write("   |   |   \n")
