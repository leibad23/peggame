import unittest

from workout import PegGame


class TestPegGame(unittest.TestCase):

    def setUp(self):
        """Initialize a PegGame instance before each test."""
        self.game = PegGame(3)

    def test_board_creation(self):
        """Test if the board is created correctly."""
        expected_board = [[1], [1, 1], [1, 1, 1]]
        self.assertEqual(self.game.create_board(), expected_board)

    def test_invalid_board_size(self):
        """Test if the game prevents a board smaller than 3."""
        with self.assertRaises(ValueError) as context:
            PegGame(2)
        self.assertEqual(str(context.exception), "Size must be greater than 2") 
        
    def test_valid_move(self):
        """Test if a peg move is executed correctly."""
        self.game.starting_position(0, 0)  # Remove a peg
        self.assertEqual(self.game.board[0][0], 0)  # Ensure the peg is removed

        self.game.move_the_peg(2, 0, 0, 0)  # Make a valid move
        self.assertEqual(self.game.board[2][0], 0)  # Old position should be empty
        self.assertEqual(self.game.board[1][0], 0)  # Jumped peg should be removed
        self.assertEqual(self.game.board[0][0], 1)  # New position should be occupied

    def test_invalid_move(self):
        """Test if an invalid move is rejected."""
        self.assertFalse(self.game.is_valid_position(0, 0, 2, 0))  # Move should be invalid initially

    def test_check_for_win(self):
        """Test win condition detection."""
        self.game.board = [[0], [0, 0], [0, 0, 1]]  # Set up a win scenario (one peg left)
        self.assertTrue(self.game.check_for_win())

    def test_no_available_moves(self):
        """Test if the game correctly detects when no moves are left."""
        self.game.board = [[1], [0, 0], [0, 0, 0]]  # No valid moves left
        self.assertTrue(self.game.check_for_win())

if __name__ == "__main__":
    unittest.main()
