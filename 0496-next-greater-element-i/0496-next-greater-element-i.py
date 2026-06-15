class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            p=0
            k=nums2.index(i)
            for j in nums2[k+1::]:
                if j>i:
                    l.append(j)
                    p=1
                    break
            if p==0:
                l.append(-1)
        return l
