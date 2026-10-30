class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        indices_stack = [] 

        for i in range(n - 1, -1, -1):

            while indices_stack and temperatures[i] >= temperatures[indices_stack[-1]]:
                indices_stack.pop()

            if indices_stack:
                result[i] = indices_stack[-1] - i

            indices_stack.append(i)
            
        return result