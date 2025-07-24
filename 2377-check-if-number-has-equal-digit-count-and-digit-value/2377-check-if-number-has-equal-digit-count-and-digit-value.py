class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            a=int(num[i])
            if num.count(str(i))!=a:
                return False
        return True
        