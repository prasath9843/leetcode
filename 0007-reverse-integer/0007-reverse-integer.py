class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Get the sign
        sign = -1 if x < 0 else 1
        x *= sign
        
        # Reverse digits
        rev = int(str(x)[::-1])
        
        # Apply sign
        rev *= sign
        
        # Check 32-bit range
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
