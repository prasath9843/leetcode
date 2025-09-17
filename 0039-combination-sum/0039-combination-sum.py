from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # base case: if total equals target, add a copy of path
            if total == target:
                res.append(list(path))
                return
            # if total exceeds target, stop exploring
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i+1 because we can reuse same element
                path.pop()  # undo the choice

        backtrack(0, [], 0)
        return res
