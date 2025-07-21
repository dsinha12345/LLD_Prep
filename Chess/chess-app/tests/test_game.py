from src.game import Game
from src.enums import Color, GameStatus
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.initial_board = [
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
        ]
        self.game.board.setup_from_string_array(self.initial_board)

    def test_initial_game_status(self):
        self.assertEqual(self.game.getGameStatus(), GameStatus.IN_PROGRESS.value)
        self.assertEqual(self.game.getNextTurn(), Color.WHITE.value)

    def test_valid_move(self):
        result = self.game.move(1, 0, 3, 0)  # Move white pawn
        self.assertEqual(result, "")
        self.assertEqual(self.game.board.get_piece(3, 0).color, Color.WHITE)

    def test_invalid_move(self):
        result = self.game.move(1, 0, 2, 0)  # Invalid move for pawn
        self.assertEqual(result, "invalid")

    def test_capture_move(self):
        self.game.move(1, 0, 3, 0)  # Move white pawn
        result = self.game.move(6, 0, 5, 0)  # Move black pawn
        self.assertEqual(result, "")
        result = self.game.move(3, 0, 4, 0)  # Move white pawn
        self.assertEqual(result, "")
        result = self.game.move(6, 1, 5, 2)  # Move black knight
        self.assertEqual(result, "")
        result = self.game.move(4, 0, 5, 1)  # Capture black knight
        self.assertEqual(result, "BN")

    def test_checkmate(self):
        # Set up a scenario for checkmate
        self.game.move(1, 0, 3, 0)  # Move white pawn
        self.game.move(6, 0, 5, 0)  # Move black pawn
        self.game.move(3, 0, 4, 0)  # Move white pawn
        self.game.move(5, 0, 4, 0)  # Move black pawn
        self.game.move(4, 0, 5, 0)  # Move white pawn
        self.game.move(4, 1, 5, 2)  # Move black knight
        self.game.move(5, 0, 6, 0)  # Move white pawn
        self.game.move(5, 2, 6, 3)  # Move black knight
        self.game.move(6, 0, 7, 0)  # Move white pawn
        self.game.move(6, 3, 7, 4)  # Move black knight
        self.game.move(7, 0, 7, 1)  # Move white pawn
        self.game.move(7, 4, 7, 5)  # Move black knight
        self.game.move(7, 1, 7, 2)  # Move white pawn
        self.game.move(7, 5, 7, 6)  # Move black knight
        self.game.move(7, 2, 7, 3)  # Move white pawn
        self.game.move(7, 6, 7, 7)  # Move black knight
        self.assertEqual(self.game.getGameStatus(), GameStatus.BLACK_WINS.value)

if __name__ == '__main__':
    unittest.main()