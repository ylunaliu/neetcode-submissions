class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0
        while left< right:
            length = right-left
            height = min(heights[left], heights[right])
            current_max = height*length
            max_water = max(max_water, current_max)
            if heights[left]<heights[right]:
                left+=1
            elif heights[right]< heights[left]:
                right-=1
            else:
                left+=1
        return max_water