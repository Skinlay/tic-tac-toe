import unittest
from io import StringIO
from tictactoe import TttView
from unittest.mock import patch


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

    # @patch('builtins.input', lambda *args: '5')
    def test_replace_number_in_list(self):
        view = TttView()

        self.listTest = "['x', '2', '3', '4', '5', '6', '7', '8', '9']"
        local_out = StringIO()
        view.placing_chois(out=local_out)

        self.assertEquals(local_out.getvalue(), self.listTest)

#       this works but i wat to compare 2 lists instead of 2 strings
#       problems i ran into:
#           -file TttView.py out.write wants a string not a list
#           -local_out is a list but wants a string
# @patch('builtins.input', lambda *args: '10')
#


if __name__ == "__main__":
    unittest.main(exit=False)

#       compares 2 list but does not work
#        self.assertListEqual(local_out.getvalue(), self.listtest)
