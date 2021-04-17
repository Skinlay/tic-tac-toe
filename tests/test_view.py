import unittest
from io import StringIO
from tictactoe import TttView


class TestTttView(unittest.TestCase):
    def test_tekeningen(self):
        view = TttView()
        local_out = StringIO()
        view.draw(out=local_out)
        self.assertEqual(local_out.getvalue(),
                         " 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 \n")

    def test_turn_incorect(self):
        view = TttView()
        view.turn = "N"
        local_out = StringIO()
        with self.assertRaises(SystemExit) as err:
            view.which_turn(out=local_out)


if __name__ == "__main__":
    unittest.main(exit=False)
