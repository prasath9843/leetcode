class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        k=[]
        for i in range(len(s)):
            if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
                l.append(s[i])
                k.append(i)
            elif s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
                l.append(s[i])
                k.append(i)
        l=l[::-1]
        p=""
        j=0
        k=set(k)
        for i in range(len(s)):
            if i in k:
                p=p+l[j]
                j+=1
            else:
                p=p+s[i]
        return p
