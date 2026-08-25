class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1. create a hash for cols, rols, and squares to store numbers 1 -9
        #2. add the numbers in the col, rols, and squares, 
        #3. if any of them are in the cols rows, and quares, return False
        #4. return True

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r //3, c//3)]):
                    return False


                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True