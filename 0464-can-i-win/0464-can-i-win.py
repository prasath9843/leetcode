class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        memo = {}

        def dfs(mask, target):
            if mask in memo:
                return memo[mask]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)

                if mask & bit == 0:
                    if i >= target or not dfs(mask | bit, target - i):
                        memo[mask] = True
                        return True

            memo[mask] = False
            return False

        return dfs(0, desiredTotal)