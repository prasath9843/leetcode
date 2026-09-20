import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        heap = [(0, float('inf'))]
        res = []
        prev = 0

        for x, neg_h, right in events:
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h:
                heapq.heappush(heap, (neg_h, right))

            cur = -heap[0][0]

            if cur != prev:
                res.append([x, cur])
                prev = cur

        return res