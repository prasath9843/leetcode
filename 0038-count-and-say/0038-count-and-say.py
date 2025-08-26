class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1, n):
            s = self.next_term(s)
        return s

    def next_term(self, s: str) -> str:
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(s[i - 1])
                count = 1
        # append the last group
        result.append(str(count))
        result.append(s[-1])
        return "".join(result)
