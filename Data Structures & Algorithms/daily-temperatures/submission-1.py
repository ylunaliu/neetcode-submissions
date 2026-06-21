class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, tem in enumerate(temperatures):
            while stack and tem > temperatures[stack[-1]]:
                old_index = stack.pop()
                days = i-old_index
                res[old_index] = days
            stack.append(i)
        return res




