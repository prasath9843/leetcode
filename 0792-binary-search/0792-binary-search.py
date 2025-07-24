class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        for i in nums:
            if i==target:
                a=1
                break
        if a==0:
            return -1
        else:
            return nums.index(i)