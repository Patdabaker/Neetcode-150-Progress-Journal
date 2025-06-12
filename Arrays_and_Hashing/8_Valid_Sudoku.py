"""
Problem: Valid Sudoku
Link: https://neetcode.io/problems/valid-sudoku?list=neetcode150
Category: Arrays & Hashing
Created on: 6/10/2025

Approach:
- Using nested for loops to check each box in board and adding them to row and column dictionary
- After row/column is complete, returns false if value > 1, then empties dictionary check next
- Checks squares the same way as row/column
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            rows = {}
            cols = {}
            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    rows[board[i][j]] = rows.get(board[i][j], 0) + 1
                    if rows[board[i][j]] > 1:
                        return False
                if board[j][i].isdigit():
                    cols[board[j][i]] = cols.get(board[j][i], 0) + 1
                    if cols[board[j][i]] > 1:
                        return False
        for i in range(0, len(board), 3):
            squares = {}
            for j in range(len(board[i])):
                if j % 3 == 0:
                    if any(value > 1 for value in squares.values()):
                        return False
                    squares = {}
                if board[i][j].isdigit():
                    squares[board[i][j]] = squares.get(board[i][j], 0) + 1
                if board[i + 1][j].isdigit():
                    squares[board[i + 1][j]] = squares.get(board[i + 1][j], 0) + 1
                if board[i + 2][j].isdigit():
                    squares[board[i + 2][j]] = squares.get(board[i + 2][j], 0) + 1
        return True
test = Solution()
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(test.isValidSudoku(board))