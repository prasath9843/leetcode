class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        l=[]
        for i in range(len(s)):
            a=(i+k)%n
            l.append(s[a])
        return "".join(l)