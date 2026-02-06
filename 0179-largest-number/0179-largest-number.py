from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str, nums))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums)
        
        # Edge case: all zeros
        return "0" if result[0] == "0" else result
