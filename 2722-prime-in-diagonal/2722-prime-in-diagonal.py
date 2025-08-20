class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        s = set()
        n = len(nums)
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        for i in range(n):
            if is_prime(nums[i][i]):
                s.add(nums[i][i])
            if is_prime(nums[i][n-i-1]):
                s.add(nums[i][n-i-1])
        
        return max(s) if s else 0
