class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        left_boundary = [-1] * len(heights)
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]]>=height:
                stack.pop()
            if stack:
                left_boundary[i] = stack[-1]
            else:
                left_boundary[i] = -1
            stack.append(i)

        #scan from right to left
        right_boundary = [len(heights)] * len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>= heights[i]:
                stack.pop()
            if stack:
                right_boundary[i] = stack[-1]
            stack.append(i)

        for i, height in enumerate(heights):
            rectangle = (right_boundary[i] - left_boundary[i]-1)*height
            largest = max(largest, rectangle)
        return largest

        
            
            #for each index i search the smallest bar encounter going right
