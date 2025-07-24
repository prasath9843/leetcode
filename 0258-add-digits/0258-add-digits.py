class Solution:
    def addDigits(self, num: int) -> int:
        a=str(num)
        b=0
        while num>=10:
            b=0
            for i in a:
                b=b+int(i)
            a=str(b)
            num=b
        return num