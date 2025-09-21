from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0 or indexDiff < 0:
            return False

        size = valueDiff + 1          # bucket width
        bucket = {}

        for i, num in enumerate(nums):
            bid = num // size         # Python's // correctly floors for negatives

            # same bucket -> difference <= valueDiff
            if bid in bucket:
                return True

            # check neighbors
            if (bid - 1) in bucket and abs(num - bucket[bid - 1]) <= valueDiff:
                return True
            if (bid + 1) in bucket and abs(num - bucket[bid + 1]) <= valueDiff:
                return True

            # insert current
            bucket[bid] = num

            # keep window of previous indexDiff elements
            if i >= indexDiff:
                old_bid = nums[i - indexDiff] // size
                bucket.pop(old_bid, None)

        return False
