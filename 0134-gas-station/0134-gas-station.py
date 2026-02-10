from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # If we cannot reach next station
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        # If total gas >= total cost → possible
        if total_tank >= 0:
            return start
        else:
            return -1
