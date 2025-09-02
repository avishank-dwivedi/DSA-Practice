class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid(r ,c ,ch):

            for i in range(9):
                if board[r][i] == ch:
                    return False
                
            for i in range(9):
                if board[i][c] == ch:
                    return False

            startRow , startCol = 3*(r//3), 3*(c // 3)
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == ch:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str , range(1,10)):
                            if is_valid(r,c,ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True
        return backtrack()
