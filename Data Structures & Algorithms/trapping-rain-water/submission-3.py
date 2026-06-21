class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        left_max = [0]*len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(len(height)):
            water = min(left_max[i], right_max[i])-height[i]
            if water>0:
                max_water +=water
        return max_water
        
        
        # max_water = 0
        
        # for i, num in enumerate(height):
        #     tallest_left = 0
        #     tallest_right = 0
        #     for l, h in enumerate(height[:i+1]):
        #         tallest_left = max(h, tallest_left)
        #     for r, h in enumerate(height[i:]):
        #         tallest_right = max(h, tallest_right)
        #     if (min(tallest_left, tallest_right) - num)>0:
        #         max_water += min(tallest_left, tallest_right) - num
        # return max_water

            
