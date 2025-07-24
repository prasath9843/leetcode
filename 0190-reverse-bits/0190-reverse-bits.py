class Solution:
    def reverseBits(self, n: int) -> int:
        a=format(n,"032b")
        a=a[::-1]
        return int(a,2)
        