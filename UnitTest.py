import unittest
from cracker_barrel_solver import solve

class TestCrackerBarrelSolver(unittest.TestCase):

    def setUp(self):
        # Set up a predefined board configuration for testing
        self.board = [
            [0], 
            [1, 1], 
            [1, 1, 1], 
            [1, 1, 1, 1],
            [1 , 1 , 1, 1 , 1]
        ]

    def test_solution_exists(self):
        solution = solve(self.board)
        self.assertGreater(len(solution), 0, "No solution found.")

    def test_solution_format(self):
        solution = solve(self.board)
        if solution:
            # Test that the solution consists of tuples (r1, c1, r2, c2)
            for move in solution[0]:
                self.assertEqual(len(move), 4)
                self.assertTrue(all(isinstance(x, int) for x in move), "All move coordinates should be integers.")

    def test_no_solution_found(self):
        # Modify the board to a state with no solution (e.g., removing pegs)
        no_solution_board = [
            [0], 
            [1, 0], 
            [0, 1, 0], 
            [0, 0, 1, 0],
            [0 , 0 , 0, 0 , 0]
        ]
        solution = solve(no_solution_board)
        self.assertEqual(len(solution), 0, "Solution was found but should not have been.")

if __name__ == '__main__':
    unittest.main()
