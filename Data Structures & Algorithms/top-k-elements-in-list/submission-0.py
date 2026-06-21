class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+=1
        sorted_items = sorted(count.items(), key = lambda item:item[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
