from collections import Counter

class Solution:

    def isValid(self, row: List[str]) -> bool:

        counter = Counter(row)
        
        for key, val in counter.items():

            if val > 1:
                if key != '.':
                    return False

        return True

    def isValidSquare(self, board: List[List[str]], row_index:int, column_index:int) -> bool:

        square = [board[i][j] for i in range(row_index, row_index + 3) for j in range(column_index, column_index + 3)]

        return self.isValid(square) 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            if not self.isValid(row): return False

        for i in range(len(board)):

            column = [board[j][i] for j in range(len(board))]

            if not self.isValid(column) : return False

        for i in range(0, len(board), 3):

            for j in range(0, len(board[0]), 3):

                if not self.isValidSquare(board, i, j) : return False

        return True

