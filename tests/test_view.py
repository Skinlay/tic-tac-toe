import unittest
from io import StringIO
from tictactoe import TttView

class TestTttView(unittest.TestCase):
    def test_tekeningen(self):
        view = TttView()
        local_out = StringIO()
        view.draw(out=local_out)
        self.assertEqual(local_out.getvalue(), "   |   |   \n---|---|---\n   |   |   \n---|---|---\n   |   |   \n")