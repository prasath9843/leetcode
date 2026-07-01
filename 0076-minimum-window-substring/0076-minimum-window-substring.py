from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(t)

        left = 0
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            if need[s[right]] > 0:
                required -= 1
            need[s[right]] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                need[s[left]] += 1
                if need[s[left]] > 0:
                    required += 1
                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]