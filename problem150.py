#Rank 1,029,876
# 17 medium, 53.6%

# 94ms, 61.18%
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tokens.reverse()
        
        while tokens:
            x = tokens.pop()
            try:
                stack.append(int(x))
                continue
            except ValueError:
                pass
            if x == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
                continue
            if x == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
                continue
            if x == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
                continue
            if x == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
                continue
        
        return stack[0]