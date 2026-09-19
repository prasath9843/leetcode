class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                length = 1

                while num + length in s:
                    length += 1

                longest = max(longest, length)

        return longest