class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(curr, open_count, close_count):
            # If the current string is valid and complete
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            # Add '(' if we still have open brackets left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            
            # Add ')' if valid (close_count < open_count)
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
