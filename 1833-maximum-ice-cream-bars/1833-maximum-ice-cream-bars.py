from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Step 1: Sort the costs
        costs.sort()
        
        count = 0
        
        # Step 2: Buy ice creams from cheapest
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        
        return count
