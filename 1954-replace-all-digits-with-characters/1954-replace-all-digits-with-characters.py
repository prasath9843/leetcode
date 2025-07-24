class Solution:
    def replaceDigits(self, s: str) -> str:
        k=""
        for i in range(len(s)):
            if s[i].isdigit():
                k+=chr(ord(s[i-1])+int(s[i]))
            else:
                k+=s[i]
        return k
        