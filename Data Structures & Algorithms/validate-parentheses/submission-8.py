class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dic = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for bracket in s:
            if bracket in "{[(":
                stack.append(bracket)
            else:
                if not stack:
                    return False

                top = stack[-1]

                if bracket_dic[bracket] != top:
                    return False

                stack.pop()

        return not stack