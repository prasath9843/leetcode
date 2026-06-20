class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        k=""
        l=[]
        for i in range(n):
            for j in range(i+1,n+1):
                k=s[i:j]
                if k==k[::-1]:
                    l.append(k)
        return (max(l,key=len))
