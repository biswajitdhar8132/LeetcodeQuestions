import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
                
        n = len(filtered_coins)
        pie_factors = []
        
        
        def precompute_lcm(index, current_lcm, elements_count):
            if index == n:
                if elements_count > 0:
                    sign = 1 if elements_count % 2 == 1 else -1
                    pie_factors.append((current_lcm, sign))
                return
            
          
            precompute_lcm(index + 1, current_lcm, elements_count)
            
            
            next_lcm = math.lcm(current_lcm, filtered_coins[index])
            precompute_lcm(index + 1, next_lcm, elements_count + 1)
            
        precompute_lcm(0, 1, 0)
        
        def count_valid_amounts(x):
            count = 0
            for lcm_val, sign in pie_factors:
                count += sign * (x // lcm_val)
            return count

        
        low = 1
        high = min(filtered_coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if count_valid_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans