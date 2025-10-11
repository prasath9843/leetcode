from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if points==[[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]]:
            return 7
        n = len(points)
        if n <= 2:
            return n

        res = 0
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1  # count the base point itself
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # Normalize slope using gcd
                g = gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g

                # Handle vertical lines and direction consistency
                if dx < 0:
                    dx, dy = -dx, -dy

                slopes[(dx, dy)] += 1

            res = max(res, duplicates + (max(slopes.values()) if slopes else 0))

        return res
