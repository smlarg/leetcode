class Solution:
    
    # 52ms, 30.41%
    def climbStairs(self, n: int) -> int:
        from math import comb
        
        num_ones = n
        num_twos = 0
        tots = 0
        while num_ones >= 0:
            tots += comb(num_ones + num_twos, num_ones)
            num_ones -= 2
            num_twos += 1
        
        return tots
    
    # uh, this is the fibonnochi sequence, btw....
    # it's all the choices one below, but with a 1 at the end, or all the choices 2 below with a 2 at the end
    # f(n) = f(n-1) + f(n-2)