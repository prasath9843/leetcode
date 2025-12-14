class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex+1
        l=[]

        num = 1
        for j in range(n):
            l.append(num)
            num = num * (n - 1 - j) // (j + 1)
        return l
