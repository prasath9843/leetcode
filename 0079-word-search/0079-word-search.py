from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            # If all letters matched
            if i == len(word):
                return True
            # Check boundaries and matching letter
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"  # temporary mark
            
            # Explore 4 directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            
            board[r][c] = temp  # backtrack
            return found
        
        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
