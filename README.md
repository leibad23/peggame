This project is a web-based Peg game using Flask as the backend framework. 
The game lets you manipulate pegs on a board and includes features like setting the board size, choosing the starting position, and moving pegs.

Requirements
Make sure to have the following Python libraries installed to run the project:

bash Copy Edit
Flask==2.1.1
You can install the dependencies using the 
requirements.txt file:

bash Copy Edit
pip install -r requirements.txt
Running the Project
Clone the repository to your local machine.
git clone -b dev https://github.com/username/peggame.git


Install the required dependencies:

bash Copy Edit
pip install -r requirements.txt
Run the Flask application:

bash Copy Edit
python app.py
Open your browser and go to http://127.0.0.1:5000/ to play the game.

How to Use the Game
Game Features:
Board Size: You can specify the board size (greater than 2) to set up the game.
Starting Position: Select a peg you want to remove as the starting position.
Move Peg: Once the starting position is set, click on a peg to select it, then click on the empty space to move it.
Winning Condition: The game checks for a win automatically after each move. If you win, it will display a congratulatory message. If no valid moves remain, the game ends.

Endpoints:
/: Home page
/get_board: Fetches the current game board and remaining moves.
/size: Sets the size of the board.
/start_position: Sets the starting position for the game.
/move_peg: Makes a move on the board.
/reset_game: Resets the game to its initial state.
Running Tests
You can test the logic of the game using the test script located in tests/test_game.py.

Here is how the tests are structured:

Test Logic:
Test Setup: The test initializes the PegGame with a default size (5).
Test Board Creation: It verifies that the board is correctly created based on the given size.
Test Valid Move: Tests valid moves to ensure the game behaves correctly when pegs are moved.
Test Win Condition: The game checks if there is exactly one peg left on the board and declares the player as the winner.
Test Invalid Move: Verifies that invalid moves are rejected.

Example Test Script: python Copy Edit
import unittest
from app import PegGame

class TestPegGame(unittest.TestCase):
    def setUp(self):
        """Initialize the game before each test"""
        self.game = PegGame(5)  # Default size is 5
        
    def test_create_board(self):
        """Test if the board is created correctly for the given size"""
        board = self.game.get_board()
        self.assertEqual(len(board), 5)
        self.assertEqual(len(board[0]), 1)
        self.assertEqual(len(board[4]), 5)

    def test_move_peg(self):
        """Test a valid peg move"""
        self.game.starting_position(0, 0)  # Set starting position
        result = self.game.move_the_peg(0, 0, 2, 0)  # Move the peg
        self.assertTrue(result)
        board = self.game.get_board()
        self.assertEqual(board[0][0], 0)  # Original position should be empty
        self.assertEqual(board[2][0], 1)  # New position should have a peg

    def test_check_win_condition(self):
        """Test win condition"""
        self.game.starting_position(0, 0)
        self.game.move_the_peg(0, 0, 2, 0)
        win_message = self.game.check_for_win()
        self.assertEqual(win_message, "Congratulations! You won!")

    def test_invalid_move(self):
        """Test an invalid peg move"""
        self.game.starting_position(0, 0)
        result = self.game.move_the_peg(0, 0, 1, 1)  # Invalid move
        self.assertFalse(result)
        board = self.game.get_board()
        self.assertEqual(board[0][0], 0)  # Original position should still be empty
Running the Tests:
Install unittest if you don't have it (it’s included by default in Python, so no installation is usually needed).

Run the test script using:

bash Copy Edit
python -m unittest tests/test_game.py
Review the results to ensure everything works correctly.

Contributing
If you'd like to contribute, feel free to fork the repository, create a new branch, and submit a pull request. Ensure that your code is well-documented and tested before submitting.

License
This project is licensed under the MIT License.
