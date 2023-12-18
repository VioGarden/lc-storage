class MinStack:

    def __init__(self):
        self.stack = [] # init stack
        self.minstack = [] # init min stack

    def push(self, val: int) -> None:
        self.stack.append(val) # append to stack
        minval = min(self.minstack[-1] if self.minstack else val, val) # find min of val or top of minstack if it exists
        self.minstack.append(minval) # minstack append

    def pop(self) -> None:
        self.stack.pop() # remove from top
        self.minstack.pop() # remove from top

    def top(self) -> int:
        return self.stack[-1] # return top of stack

    def getMin(self) -> int:
        return self.minstack[-1] # return top of minstack (minimum value)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()