from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()

        for a, b, c in permutations(digits, 3):
            if a == 0:          # no leading zero
                continue
            if c % 2 != 0:      # must be even
                continue

            num = a * 100 + b * 10 + c
            result.add(num)

        return sorted(result)
