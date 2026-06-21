class Solution:
    def isValid(self, s: str) -> bool:
        res = ""
        stack = []
        braket_dic = {"}": "{", "]": "[", ")":"("}
        for braket in s:
            if braket in "{([":
                stack.append(braket)
            if braket in "})]":
                if not stack:
                    return False
                else: 
                    top = stack[-1]
                if braket_dic[braket] != top:
                    print(braket, braket_dic[braket])
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False

            