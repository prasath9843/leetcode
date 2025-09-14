class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=min(nums)
        b=max(nums)
        l=[]
        for i in range(a,b+1):
            if i in nums:
                l.append([nums.count(i),i])
        l.sort(reverse=True)
        p=[]
        for i in range(k):
            p.append(l[i][1])
        return p