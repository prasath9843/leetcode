from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        
        for i in range(1 << n):   # 2^n numbers
            gray = i ^ (i >> 1)
            result.append(gray)
            
        return result