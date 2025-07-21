class Solution:
    def twoSum(self, nums, target):
        a=len(nums)
        l=[]
        for i in range(a):
            for j in range(i):
                if nums[i]+nums[j]==target:
                    return [i,j]
        