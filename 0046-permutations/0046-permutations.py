class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack(path, used)

                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return res