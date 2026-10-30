class MinStack:

    def __init__(self):
        self.stack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        top_value = self.stack[-1]
        return top_value
        

    def getMin(self) -> int:
        min_value = min(self.stack)
        return min_value
        
