class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        
        for i, num in enumerate(height):
            tallest_left = 0
            tallest_right = 0
            for l, h in enumerate(height[:i+1]):
                tallest_left = max(h, tallest_left)
            for r, h in enumerate(height[i:]):
                tallest_right = max(h, tallest_right)
            if (min(tallest_left, tallest_right) - num)>0:
                max_water += min(tallest_left, tallest_right) - num
        return max_water

            
