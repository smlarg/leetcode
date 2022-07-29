["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]
["MyQueue","push","pop","empty"]
[[],[1],[],[]]
["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
[[],[1],[2],[3],[4],[],[5],[],[],[],[]]


# 55ms, 23.39%, low memory variance oddly
class MyQueueAmoritized:

    def __init__(self):
        self.queue = []
        self.counter = 0
        self.l = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.l +=1
        

    def pop(self) -> int:
        if self.l - self.counter < self.l//4:
            self.queue = self.queue[self.counter:]
            self.l -= self.counter
            self.counter -= self.counter
        self.counter += 1
        return self.queue[self.counter -1]

    def peek(self) -> int:
        return self.queue[self.counter]
        

    def empty(self) -> bool:
        return self.counter == self.l

# 42ms, 60.16%
class MyQueueAmoritizedTunedABit:

    def __init__(self):
        self.queue = []
        self.counter = 0
        self.l = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.l +=1
        

    def pop(self) -> int:
        if (self.l - self.counter < self.l//4) and self.l > 16:
            self.queue = self.queue[self.counter:]
            self.l -= self.counter
            self.counter -= self.counter
        self.counter += 1
        return self.queue[self.counter -1]

    def peek(self) -> int:
        return self.queue[self.counter]
        

    def empty(self) -> bool:
        return self.counter == self.l

#52ms, 30.79%, so
class MyQueueUpAndDown:

    def __init__(self):
        self.stackNormal = []
        self.stackUpsideDown = []

    def push(self, x: int) -> None:
        self.stackNormal.append(x)

    def pop(self) -> int:
        if self.stackUpsideDown: return self.stackUpsideDown.pop()
        while self.stackNormal:
            self.stackUpsideDown.append(self.stackNormal.pop())
        return self.stackUpsideDown.pop()

    def peek(self) -> int:
        if self.stackUpsideDown: return self.stackUpsideDown[-1]
        return self.stackNormal[0]
        
    def empty(self) -> bool:
        return not (self.stackNormal or self.stackUpsideDown)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# I didn't submit this, but, after seeing the fast submitions....
class MyHackyQueue:

    def __init__(self):
        self.hacky_queue = []
        self.reversed = False

    def push(self, x: int) -> None:
        if not self.reversed:
            self.hacky_queue.append(x)
        else:
            self.hacky_queue.reverse()
            self.reversed = False
            self.hacky_queue.append(x)

    def pop(self) -> int:
        if self.reversed:
            return self.hacky_queue.pop()
        else:
            self.hacky_queue.reverse()
            return self.hacky_queue.pop()
            self.reversed = True
        

    def peek(self) -> int:
        if self.reversed:
            return self.hacky_queue[-1]
        else:
            return self.hacky_queue[0]
        

    def empty(self) -> bool:
        return len(self.hacky_queue) == 0
        
# theses were from the metrics page, absolute trash, i don't get it

this is retarded right? it got 32ms. wtf??

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)



and this is 31ms????? no, no, fuck this

class MyQueue:

    def __init__(self):
        self.stack=[]
        self.t=None

    def push(self, x: int) -> None:
        if len(self.stack)==0:
            self.t=x
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)==1:
            self.t=None
            return self.stack.pop()
        
        temp=[]
        while len(self.stack)>1:
            temp.append(self.stack.pop())
        self.t=temp[-1]
        re=self.stack.pop()
        while len(temp)>0:
            self.stack.append(temp.pop())
        return re

    def peek(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.stack)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()