class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        # Boolean array, True = prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Only go till sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Start crossing out from i*i (smaller multiples already handled)
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
