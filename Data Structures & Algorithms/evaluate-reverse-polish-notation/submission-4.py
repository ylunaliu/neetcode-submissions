import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_mapping = {"+":operator.add, "-":operator.sub, "/": operator.truediv, "*":operator.mul}
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                number1 = stack[-1]
                stack.pop()
                number2 = stack[-1]
                stack.pop()
                ans = operator_mapping[token](int(number2), int(number1))
                stack.append(ans)

        return int(stack[-1])

    

            