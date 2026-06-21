class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position = sorted(zip(position, speed), reverse=True)
        stack = [] #times of fleet

        for index, (position, speed) in enumerate(sorted_position):
            time_target = (target - position)/speed
            if index==0:
                stack.append(time_target)
            if stack:
                if(time_target>stack[-1]):
                    stack.append(time_target)
                    #can form a fleet with the car ahead
        return len(stack)


   