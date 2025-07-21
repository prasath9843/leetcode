class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0   # to count balanced strings
        balance = 0 # to track difference between L and R

        for char in s:
            if char == 'L':
                balance += 1
            else:  # char == 'R'
                balance -= 1
            
            if balance == 0:
                count += 1  # found a balanced part

        return count
