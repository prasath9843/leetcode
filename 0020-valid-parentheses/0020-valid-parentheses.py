class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
        return s == ''