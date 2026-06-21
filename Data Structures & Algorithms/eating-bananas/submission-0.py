import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the hour is number of bananas//eating rate ceil(pile/k)
        # Need to find the fastest k to eat all bananas
        # If I finished, I cannot move on to the next pile
        # h is always greater than the length of piles
        # upper bound is max number of pile

        upper_bound_k = max(piles)
        lower_bound_k = 1
        fastest_time = float('inf')
        stack = []
        res_k = -1

        while lower_bound_k < upper_bound_k:
            medium_k = (lower_bound_k + upper_bound_k)//2
            hour_needed = 0
            for pile in piles:
                time = math.ceil(pile/medium_k)
                hour_needed+=time
            if hour_needed > h:
                lower_bound_k = medium_k +1
            if(hour_needed <= h):
                upper_bound_k = medium_k

        return lower_bound_k
