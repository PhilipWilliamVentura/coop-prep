# Pattern: Bactracking using dfs
# Time: O(m * (4^n)) | Space: O(n) where m is the num of cells in the board and n the len(word)
# Tripped up on: store 4 dfs results in res, remove visits then return res.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visit or board[r][c] != word[i]:
                return
            if i == len(word) - 1:
                return True
            visit.add((r, c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visit.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False