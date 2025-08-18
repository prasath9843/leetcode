class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        k=0
        if(a<b):
            p=a
        else:
            p=b
        for i in range(1,p+1):
            if (a%i==0 and b%i==0):
                k+=1
        return k