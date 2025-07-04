#The solution uses TrieNode/PrefixTree to avoid the time limit exception
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        #point a pointer to the self
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)
        #to eliminate duplicates, keep result as a set
        result = set()
        visited = set()
        rows = len(board)
        cols = len(board[0])
        dirs = [(0,-1), (0,1), (-1,0), (1,0)]

        def dfs(r, c, node, word,):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                or (board[r][c] not in node.children) or ((r,c) in visited)):
                return 
                 
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                result.add(word)
                node.is_word = False  # prevent duplicate work
            for d in dirs:
                new_r, new_c = r+d[0], c+d[1]
                dfs(new_r, new_c, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        
        return list(result)