# Pattern: Prefix tree (Hash map)
# Time: O(m * n * 4 * (3^(t-1)) + s
# Space: O(s)
# Where m is the number of rows, n is the number of columns, t is the maximum length of any word in the array words and s is the sum of the lengths of all the words.
# Tripped up on: Use dfs (4 options) with set visit to go through board[r][c] and check prefix with Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)