
# 126ms, 68.47%
# there is another peak at 100ms, maybe using int(ch) to index an array of records
# It's not worth finding out
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            entries = []
            for ch in row:
                if ch != ".":
                    entries.append(ch)
            if len(set(entries)) != len(entries): return False
        
        for i in range(9):
            entries = []:
            for row in board:
                ch = row[i]
                if ch != ".":
                    entries.append(ch)
            if len(set(entries)) != len(entries): return False
        
        for i in range(3):
            rows = [board[3*i], board[3*i+1], board[3*i+2]]
            for j in range(3):
                columns = [3*j, 3*j+1, 3*j+2]
                entries = []
                for row in rows:
                    for col in columns:
                        if row[col] != ".":
                            entries.append(row[col])
                if len(set(entries)) != len(entries): return False
        
        return True