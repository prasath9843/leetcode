class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        o=[0]
        for i in s:
            if i not in l:
                l.append(i)
            else:
                k=0
                while k==0:
                    if l[0]==i:
                        l.pop(0)
                        l.append(i)
                        break
                    else:
                        l.pop(0)
            o.append(len(l))
        return max(o)  
        