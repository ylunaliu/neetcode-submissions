class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, tem in enumerate(temperatures):
            while stack and tem > temperatures[stack[-1]]:
                old_tem = stack[-1]
                stack.pop()
                days = i-old_tem
                res[old_tem] = days
            stack.append(i)
        return res




