# 8 hard, 57.9%

# slowish, but works
# 238ms, 15.95%, median is about 120ms, memory 16.2Mb, 15.66%, correct is about 15.5Mb
class Solution:
    def calculate(self, s: str) -> int:
    
        return self.calculate2(s,0)[0]
    
    def calculate2(self,s: str, i):
        
        l = len(s)
        
        parenthesesCounter  = 0
        
        numStack = []
        opStack = []
        lastWasOp = False
        needToNegate = False
        
        # find a leading negation:
        while s[i] == ' ' and i < l:
            i+=1
        if i >= l:
            raise Exception
        if s[i] == "-":
            needToNegate = True
            i +=1
        
        while i < l:
            while i < l and s[i] == ' ':
                i+=1
            if i == l: break
            if s[i] == "(":
                i +=1
                if i >= l: raise Exception()
                num, i = self.calculate2(s,i)
                numStack.append( num )
                if needToNegate:
                    numStack[-1]*=-1
                    needToNegate = False
                lastWasOp = False
                if i >= l: break
            if s[i] == ")":
                i += 1
                break
            if s[i] == "+":
                opStack.append("+")
                lastWasOp = True
                i += 1
                if i == l: break
            if s[i] == "-":
                if lastWasOp:
                    needToNegate = True
                    lastWasOp = False
                else:
                    opStack.append("-")
                    lastWasOp = True
                i +=1
                if i >= l: break
            if s[i].isnumeric():
                start = i
                while i < l and s[i].isnumeric():
                    i +=1
                numStack.append(int(s[start:i]))
                lastWasOp = False
                if needToNegate:
                    numStack[-1]*=-1
                    needToNegate = False
                if i >= l: break
        
        if len(numStack) != len(opStack) +1:
            raise Exception()
        
        numStack.reverse()
        opStack.reverse()
        
        result = numStack.pop()
        
        while numStack:
            num = numStack.pop()
            op = opStack.pop()
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            else:
                raise Exception()
        
        return result, i


# oh, right, obviously, reversing the stacks was an indulgence
# 135ms, 55.70%, fine
class Solution:
    def calculate(self, s: str) -> int:
    
        return self.calculate2(s,0)[0]
    
    def calculate2(self,s: str, i):
        
        l = len(s)
        
        parenthesesCounter  = 0
        
        numStack = []
        opStack = []
        lastWasOp = False
        needToNegate = False
        
        # find a leading negation:
        while s[i] == ' ' and i < l:
            i+=1
        if i >= l:
            raise Exception
        if s[i] == "-":
            needToNegate = True
            i +=1
        
        while i < l:
            while i < l and s[i] == ' ':
                i+=1
            if i == l: break
            if s[i] == "(":
                i +=1
                if i >= l: raise Exception()
                num, i = self.calculate2(s,i)
                numStack.append( num )
                if needToNegate:
                    numStack[-1]*=-1
                    needToNegate = False
                lastWasOp = False
                if i >= l: break
            if s[i] == ")":
                i += 1
                break
            if s[i] == "+":
                opStack.append("+")
                lastWasOp = True
                i += 1
                if i == l: break
            if s[i] == "-":
                if lastWasOp:
                    needToNegate = True
                    lastWasOp = False
                else:
                    opStack.append("-")
                    lastWasOp = True
                i +=1
                if i >= l: break
            if s[i].isnumeric():
                start = i
                while i < l and s[i].isnumeric():
                    i +=1
                numStack.append(int(s[start:i]))
                lastWasOp = False
                if needToNegate:
                    numStack[-1]*=-1
                    needToNegate = False
                if i >= l: break
        
        if len(numStack) != len(opStack) +1:
            raise Exception()
        
        #numStack.reverse()
        #opStack.reverse()
        
        #result = numStack.pop()
        
        result = numStack[0]
        j = 0
        l = len(opStack)
        while j < l:
            num = numStack[j+1]
            op = opStack[j]
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            else:
                raise Exception()
            j += 1
        
        return result, i