from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = {}
            for j in range(9):
                if board[i][j] in seen:
                    print("first for")
                    return False
                if board[i][j] != ".":
                    seen[board[i][j]] = True
        for i in range(9):
            seen = {}
            for j in range(9):
                if board[j][i] in seen:
                    print("second for")
                    return False
                if board[j][i] != ".":
                    seen[board[j][i]] = True
        for i in range(3):
            for j in range(3):
                seen = {}
                for k in range(3):
                    for l in range(3):
                        if board[k+j*3][l+i*3] in seen:
                            return False
                        if board[k+j*3][l+i*3] != ".":
                            seen[board[k+j*3][l+i*3]] = True
        return True
sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))