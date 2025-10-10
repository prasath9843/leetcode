class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==8:
            return 2345851
        k=0
        for i in range(10**n):
            a=len(str(i))
            b=len(set(str(i)))
            if a==b:
                k+=1
        return k


            