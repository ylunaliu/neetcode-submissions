class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        #moving window = nums[left:right]
        left = 0
        right = left+k
        while right <= len(nums):
            res.append(max(nums[left:right])) #append each maximum
            left+=1
            right =left+k
        return res
        

