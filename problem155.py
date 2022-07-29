# 80ms, 71.39%, some variance in memory but I'm not going to worry about it
# no, I read the other solutions and yes I am, let's see here
# 18.2Mb, 29.00%
class MinStack:

    def __init__(self):
        self.actual_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.actual_stack.append(val)
        if self.min_stack: self.min_stack.append(min(val,self.min_stack[-1]))
        else: self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.actual_stack.pop()

    def top(self) -> int:
        return self.actual_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# yeup
# 89ms, 60.72%, 17.8Mb, 71.75%
# so regular old speed/space trade off (albeit a pretty low-stakes one)
class MinStack:

    def __init__(self):
        self.actual_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.actual_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: self.min_stack.append(val)

    def pop(self) -> None:
        r = self.actual_stack.pop()
        if self.min_stack[-1] == r:
            self.min_stack.pop()
        return r

    def top(self) -> int:
        return self.actual_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()