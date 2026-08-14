class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for col in row:
                if col == ".":
                    continue
                if col in seen:
                    return False
                seen.add(col)
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        for square in range(0,9):
            seen = set()
            for i in range(0,3):
                for j in range(0,3):
                    row = i + 3 * (square // 3)
                    col = j + 3 * (square % 3)
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

        

        
