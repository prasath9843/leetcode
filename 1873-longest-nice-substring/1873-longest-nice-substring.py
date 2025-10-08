class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        # Set of characters in current string
        char_set = set(s)
        
        for i, c in enumerate(s):
            # If the opposite case of c is not in the set, split here
            if c.swapcase() not in char_set:
                # Recur on left and right parts
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                # Return the longer one
                return left if len(left) >= len(right) else right
        
        # If we never split, the whole string is nice
        return s
