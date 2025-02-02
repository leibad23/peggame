from flask import Flask, jsonify, request, render_template
from collections import deque

app = Flask(__name__)

class PegGame:
    def __init__(self, size):
        if size <= 2:
            raise ValueError("Size must be greater than 2")
        
        self.size = size
        self.remaining_move = (self.size) * (self.size + 1) // 2 - 1
        self.board = self.create_board()
        self.total_of_ones = deque()
        self.start_selected = False  # Track if the starting position is selected

    def create_board(self):
        return [[1] * (i) for i in range(1, self.size + 1)]

    def get_board(self):
        return self.board
    
    def set_number_of_pegs(self, num):
        if num <= 2:
            return {"status": "error", "message": "Size must be greater than 2"}
        self.__init__(num)  # Reset the game with new size
        return {"status": "success", "message": f"Game reset with size {num}"}

    def starting_position(self, row, col):
        if self.start_selected:
            return {"status": "error", "message": "Starting position already set."}
        
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
            self.board[row][col] = 0  # Remove the peg
            self.start_selected = True
            win_message = self.check_for_win()  # Check for win condition immediately
            return {"status": "success", "win_message": win_message}
        
        return {"status": "error", "message": "Invalid starting position."}

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
            return True
        return False

    def check_for_win(self):
        self.total_of_ones.clear()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    self.total_of_ones.append((i, j))

        if len(self.total_of_ones) == 1:
            return "Congratulations! You won!"
        
        possible_moves = 0
        for x, y in self.total_of_ones:
            for dx, dy in [(2, 0), (0, 2), (-2, 0), (0, -2), (2, 2), (-2, -2)]:
                nx, ny = x + dx, y + dy
                if self.is_valid_position(x, y, nx, ny):
                    possible_moves += 1
        
        if possible_moves == 0:
            return "No more valid moves available. Game over!"
        
        return None

@app.route('/')
def index():
    return render_template("templates/peggame.html")

@app.route('/get_board', methods=['GET'])
def get_board():
    return jsonify({"board": game.get_board(), "remaining_moves": game.remaining_move})

@app.route('/size', methods=['POST'])
def set_pegs():
    data = request.json
    if 'size' not in data:
        return jsonify({"status": "error", "message": "Size parameter missing"}), 400

    response = game.set_number_of_pegs(int(data["size"]))
    return jsonify(response)




@app.route('/start_position', methods=['POST'])
def start_position():
    data = request.json
    result = game.starting_position(data['row'], data['col'])
    return jsonify(result)



@app.route('/move_peg', methods=['POST'])
def move_peg():
    data = request.json
    if game.move_the_peg(data['cR'], data['cC'], data['nR'], data['nC']):
        win_message = game.check_for_win()
        return jsonify({"status": "success", "board": game.get_board(), "win_message": win_message})
    return jsonify({"status": "error", "message": "Invalid move"}), 400

@app.route('/reset_game', methods=['POST'])
def reset_game():
    global game
    game = PegGame(game.size)  # Reset with the current board size
    return jsonify({"status": "success", "message": "Game reset successfully"})

if __name__ == '__main__':
    game = PegGame(5)  # Default board size
    app.run(debug=True)
