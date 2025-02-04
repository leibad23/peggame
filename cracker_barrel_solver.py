def set_position(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[row]):
        board[row][col] = 0  # Remove the peg
        return board
    return False

def is_valid_position(board, currR, currC, newR, newC):
    if not (0 <= currR < len(board) and 0 <= currC < len(board[currR])):
        return False
    if not (0 <= newR < len(board) and 0 <= newC < len(board[newR])):
        return False
    if board[currR][currC] != 1 or board[newR][newC] != 0:
        return False
    diff_r = abs(currR - newR)
    diff_c = abs(currC - newC)
    if not ((diff_r == 2 and diff_c == 0) or (diff_r == 2 and diff_c == 2) or (diff_r == 0 and diff_c == 2)):
        return False
    inBetweenR = (currR + newR) // 2
    inBetweenC = (currC + newC) // 2
    if board[inBetweenR][inBetweenC] != 1:
        return False
    return True

def move_the_peg(board, cR, cC, nR, nC):
    inBetweenR = (cR + nR) // 2
    inBetweenC = (cC + nC) // 2
    board[cR][cC] = 0
    board[nR][nC] = 1
    board[inBetweenR][inBetweenC] = 0
    return board

# Define a more explicit triangular board for Cracker Barrel (with a hole in the middle)
board = [
    [1], 
    [1, 1], 
    [1, 1, 1], 
    [1, 1, 1, 1],
    [1 , 1 , 1, 1 , 1]
]

def solve(board):
    res, sol = [], []
    seen = set()
    
    set_position_on_board = set_position(board , 6  , 0)
    
    if set_position_on_board:

            def helper(board):
                # Base case: check if there's only one peg left on the board
                if sum([sum(row) for row in board]) == 1:  # Only one peg left
                    res.append(sol[:])  # Store the move sequence
                    return

                # Convert the board to a tuple for checking if this state has been visited
                board_tuple = tuple(tuple(row) for row in board)
                if board_tuple in seen:
                    return
                seen.add(board_tuple)

                # Explore all valid moves
                for r in range(len(board)):
                    for c in range(len(board[r])):
                        if board[r][c] == 1:  # If there's a peg here
                            for dr, dc in [(2, 0), (0, 2), (-2, 0), (0, -2), (2, 2), (-2, -2)]:
                                nr, nc = r + dr, c + dc
                                if is_valid_position(board, r, c, nr, nc):
                                    # Make a copy of the board to explore the move
                                    new_board = [row[:] for row in board]
                                    move_the_peg(new_board, r, c, nr, nc)
                                    
                                    # Record the move (from (r, c) to (nr, nc))
                                    sol.append((r, c, nr, nc))

                                    # Recursively solve for the new board
                                    helper(new_board)

                                    # Backtrack, remove the last move
                                    sol.pop()

            # Start the recursive process
            helper(set_position_on_board)

            return res
    else: 
        
        print("\nEnter valid start postition\n")

# Run the solver and print the solution sequence (moves to win)
solution = solve(board)

# Print the sequence of moves
if solution:
   
    for move in solution[0]:
        print(f"Move from ({move[0]}, {move[1]}) to ({move[2]}, {move[3]})")
else:
    print("\nNo solution found.\n")
