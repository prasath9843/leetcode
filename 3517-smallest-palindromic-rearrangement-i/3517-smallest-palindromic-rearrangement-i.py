class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        count = Counter(s)
        
        first_half = []
        middle = ""
        
        # Build palindrome
        for ch in sorted(count.keys()):
            freq = count[ch]
            
            # Add half to first part
            first_half.append(ch * (freq // 2))
            
            # If odd frequency → middle char
            if freq % 2 == 1:
                middle = ch
        
        first_half = "".join(first_half)
        
        # Mirror
        return first_half + middle + first_half[::-1]
