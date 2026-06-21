class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_sorted = sorted(nums)
        res = []
        for i, num in enumerate(num_sorted):
            left = i+1
            right = len(num_sorted)-1
            if i > 0 and num_sorted[i] == num_sorted[i - 1]:
                continue
            while left<right:
                sum_res = num+ num_sorted[left] + num_sorted[right]
                if sum_res>0:
                    right-=1
                if sum_res<0:
                    left +=1
                if sum_res==0:
                    res.append([num, num_sorted[left], num_sorted[right]])
                    left+=1
                    right-=1
                    while left < right and num_sorted[left] == num_sorted[left - 1]:
                        left += 1
                    while left < right and num_sorted[right] == num_sorted[right + 1]:
                        right -= 1
        return res


            # -a = b+c
