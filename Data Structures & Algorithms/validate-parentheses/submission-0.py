class Solution:
    def isValid(self, s: str) -> bool:
        dict ={
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []

        for par in s:
            if par in dict:
                if stack and stack[-1] == dict[par]:
                    stack.pop()
                else:
                    return False
            else: stack.append(par)

        return not stack