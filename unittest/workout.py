from collections import deque


class PegGame:
    def __init__(self, size):
        if size <= 2:
            raise ValueError("Size must be greater than 2")
        
        self.size = size
        self.remaining_move = self.size * (self.size + 1) // 2 - 1
        self.board = self.create_board()
        self.total_of_ones = deque()
        

    def create_board(self):
            return [[1] * (i) for i in range(1, self.size + 1)]

            

    def display(self):
        
            for i in range(self.size):
                print(" " * (self.size - i), end="")  # Indentation for pyramid alignment
                for j in range(i + 1):
                    print(self.board[i][j], end=" ")  # Print each peg with spacing
                print()  # Move to the next line
            print(f"Remaining Pegs: {self.remaining_move}")

    def starting_position(self, row, col):
        
            if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
                self.board[row][col] = 0
                return True
            else:
                print("Invalid position. Please choose a valid row and column.")
                return False

    def is_valid_position(self, currR, currC, newR, newC):
        
            if not (0 <= currR < len(self.board) and 0 <= currC < len(self.board[currR])):
                return False
            if not (0 <= newR < len(self.board) and 0 <= newC < len(self.board[newR])):
                return False
            if self.board[currR][currC] != 1 or self.board[newR][newC] != 0:
                return False
            diff_r = abs(currR - newR)
            diff_c = abs(currC - newC)
            if not ((diff_r == 2 and diff_c == 0) or (diff_r == 2 and diff_c == 2) or (diff_r == 0 and diff_c == 2)):
                return False
            inBetweenR = (currR + newR) // 2
            inBetweenC = (currC + newC) // 2
            if self.board[inBetweenR][inBetweenC] != 1:
                return False
            return True

    def move_the_peg(self, cR, cC, nR, nC):
        
            if self.is_valid_position(cR, cC, nR, nC):
                inBetweenR = (cR + nR) // 2
                inBetweenC = (cC + nC) // 2
                self.board[cR][cC] = 0
                self.board[nR][nC] = 1
                self.board[inBetweenR][inBetweenC] = 0
                self.remaining_move -= 1
                self.display()

    def check_for_win(self):
            self.total_of_ones.clear()
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 1:
                        self.total_of_ones.append((i, j))
            if len(self.total_of_ones) == 1:
                print("\n Congratulations! You won!")
                return True
            possible_moves = 0
            for x, y in self.total_of_ones:
                for dx, dy in [(2, 0), (0, 2), (-2, 0), (0, -2), (2, 2), (-2, -2)]:
                    nx, ny = x + dx, y + dy
                    if self.is_valid_position(x, y, nx, ny):
                        possible_moves += 1
            print(f"Number of potential moves you could make: {possible_moves}")
            if possible_moves == 0:
                return True
            return None

    def play_game(self):
        
            self.starting_position(1, 0)
            while True:
                game_statue = self.check_for_win()
                
                if game_statue == True:
                    break
                
                self.display()
                
                try:
                    x = int(input("Select peg row: "))
                    y = int(input("Select peg col: "))
                    nx = int(input("Select target peg row: "))
                    ny = int(input("Select target peg col: "))
                    self.move_the_peg(x - 1, y - 1, nx - 1, ny - 1)
                except ValueError:
                    print("\nInvalid input, only use numbers\n")
            if self.remaining_move >= 3:
                print("Good Try!!")
            elif self.remaining_move == 2:
                print("You almost had it!")
            elif self.remaining_move == 1:
                print("Wow, teach me your ways!")

if __name__ == "__main__":
        game = PegGame(3)
        game.play_game()
