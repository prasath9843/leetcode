class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            k=0
            for j in nums:
                if j<i:
                    k+=1
            l.append(k)
        return l