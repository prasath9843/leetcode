class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=[]
        a=len(nums)
        for i in range(a):
            for j in range(i+1,a):
                if nums[i]==nums[j] and i<j:
                    l.append([i,j])
        return len(l)