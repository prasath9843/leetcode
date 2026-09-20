class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n):
            dp[i] = i

            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]