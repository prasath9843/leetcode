class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                cur = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = cur

            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))