class Solution():
    def isValidSudoku(self, board):

        def isRowValid(board): # Checks rows
            for row in range(len(board)):
                for col in range(len(board[0])):
                    for currentRow in range(col + 1, len(board[0])):
                        if board[row][col] != "." and board[row][currentRow] != ".":
                            if board[row][col] == board[row][currentRow]:
                                return False
            return True

        def isColumnValid(board): # checks columns
            for row in range(len(board)):
                 for col in range(len(board[0])):
                     for currentCol in range(row + 1, len(board[0])):
                         if board[row][col] != "." and board[currentCol][col] != ".":
                             if board[row][col] == board[currentCol][col]:
                                 return False
            return True

        def isGridValid(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    submatrix = [row[j:j + 3] for row in board[i: i + 3]]
                    tempList = submatrix  # 3 by 3 grid
                    for row in range(len(tempList)): # checks grid
                        for col in range(len(tempList[0])):
                            for check_row in range(row, len(tempList)):
                                for check_col in range(len(tempList[0])):
                                    if row == check_row and col == check_col:
                                        continue
                                    else:
                                        if tempList[row][col] != "." and tempList[check_row][check_col] != ".":
                                            if tempList[row][col] == tempList[check_row][check_col]:
                                                return False
            return True

        if len(board) != 9 or len(board[0]) != 9:
            return False

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not (1 <= int(board[i][j]) <= 9):
                        return False
        return isRowValid(board) and isColumnValid(board) and isGridValid(board)
sol = Solution()
print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]))
