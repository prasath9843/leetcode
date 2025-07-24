class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if nums.count(i)<2:
                s+=i
        return s