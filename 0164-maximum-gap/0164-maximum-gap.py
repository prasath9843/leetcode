class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l=[]
        nums.sort()
        for i in range(1,len(nums)):
            l.append(abs(nums[i-1]-nums[i]))
        return max(l)
        