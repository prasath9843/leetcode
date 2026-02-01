class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(1000):
            if (4**i)==n:
                return True
        return False
        