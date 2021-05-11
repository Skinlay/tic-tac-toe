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

    def test_turn_incorrect(self):
        view = TttView()
        view.turn = "N"
        local_out = StringIO()
        with self.assertRaises(SystemExit) as err:
            view.which_turn(out=local_out)

    def test_replace_number_in_list(self):
        # maak een nieuw TttView aan
        view = TttView()
        # het reseltaat dat ik verwacht
        listtest = ["x", "2", "3", "4", "5", "6", "7", "8", "9"]
        # simuleer een ingevoerd antwoord met een vaste waarde
        view.antwoord = 0
        # voer de functie uit die je wilt testen
        view.placing_choice()
        # vergelijkt twee lijsten om te kijken of het veranderd zo als verwacht
        self.assertListEqual(view.list, listtest)

    @patch('builtins.input', lambda *args: '0')
    def test_input_validation_0(self):
        # maak een vers nieuw object
        view = TttView()
        # vraag user input om te zien of ons antwoord geaccepteerd wordt
        view.user_input()
        # controleer of ons antwoord inderdaad niet geaccepteerd wordt
        self.assertNotEqual(view.antwoord, -1)

    @patch('builtins.input', lambda *args: 'a')
    def test_input_validation_a(self):
        # maak een vers nieuw object
        view = TttView()
        # vraag user input om te zien of ons antwoord geaccepteerd wordt
        view.user_input()
        # controleer of ons antwoord inderdaad niet geaccepteerd wordt
        self.assertNotEqual(view.antwoord, 'a')

    @patch('builtins.input', lambda *args: '10')
    def test_input_validation_10(self):
        # maak een vers nieuw object
        view = TttView()
        # vraag user input om te zien of ons antwoord geaccepteerd wordt
        view.user_input()
        # controleer of ons antwoord inderdaad niet geaccepteerd wordt
        self.assertNotEqual(view.antwoord, 9)


if __name__ == "__main__":
    unittest.main(exit=False)

#       @patch('builtins.input', lambda *args: '10')
