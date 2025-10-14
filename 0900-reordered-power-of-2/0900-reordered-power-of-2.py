class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Helper: return the sorted string of digits of a number
        def count_digits(x):
            return ''.join(sorted(str(x)))
        
        # Sorted digits of n
        target = count_digits(n)
        
        # Compare with all powers of 2 up to 10^9 (since 2^30 < 10^9 < 2^31)
        for i in range(31):
            if count_digits(1 << i) == target:
                return True
        return False
