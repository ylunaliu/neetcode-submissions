class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Include all permutations, but not repeat
        res = []
        def backtrack(pos, cur, chosen):
            if len(cur) == len(nums):
                res.append(cur.copy())
        
            for i in range(len(nums)):
                if chosen[i] == True:
                    continue
                cur.append(nums[i])
                chosen[i] = True
                backtrack(i+1, cur, chosen)
                cur.pop()
                chosen[i] = False

        backtrack(0, [], [False]*len(nums))
        return res
