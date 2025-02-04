# Cracker Barrel Peg Game Solver

This project solves the Cracker Barrel Peg Game (a variation of the solitaire game) on a triangular board. The goal is to determine the sequence of moves that will leave only one peg remaining on the board.

### Features:
- Solves the game starting from a predefined board configuration.
- Returns the sequence of moves required to win the game.
- The algorithm uses recursion to explore possible moves and backtrack when necessary.

### Problem Description:
- The game board consists of a triangle of pegs, with one hole (empty space) in the middle.
- A valid move consists of jumping a peg over an adjacent peg into an empty space, removing the jumped peg.
- The goal is to leave just one peg remaining on the board.

### How It Works:
1. **`set_position(board, row, col)`**: Sets the position of the peg to 0 (removes it from the board).
2. **`is_valid_position(board, currR, currC, newR, newC)`**: Checks if a move is valid by ensuring the destination is empty and the jump is over an adjacent peg.
3. **`move_the_peg(board, cR, cC, nR, nC)`**: Moves a peg from one position to another and removes the jumped peg.
4. **`solve(board)`**: The main recursive function that attempts to solve the board by exploring all valid moves.

### Requirements:
- Python 3.x

### How to Run:
1. Clone the repository or download the script `cracker_barrel_solver.py`.
2. Run the script with Python:

```bash
python cracker_barrel_solver.py
