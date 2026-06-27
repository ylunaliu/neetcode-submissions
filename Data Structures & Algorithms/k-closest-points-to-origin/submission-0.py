class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        #we want to pop k times
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        #linear time

        heapq.heapify(minHeap)
        res = []
        while k>0:
            res.append(heapq.heappop(minHeap)[1:])
            k-=1
        return res

        
            