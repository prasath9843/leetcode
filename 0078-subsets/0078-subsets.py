from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # add the current subset
            res.append(path[:])

            # try adding each element starting from `start`
            for i in range(start, len(nums)):
                path.append(nums[i])       # choose
                backtrack(i + 1, path)    # explore
                path.pop()                # un-choose (backtrack)

        backtrack(0, [])
        return res
