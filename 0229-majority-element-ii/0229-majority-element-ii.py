class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        a = len(nums) // 3
        return [num for num, freq in count.items() if freq > a]
