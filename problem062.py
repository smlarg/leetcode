#?
#It takes a *little* bit of care to do the factorial without overflow
#n*(n-1)//2*(n-2)//3*...*(n-k+1)//k
# with n = (m+n-2) and k = min(m-1,n-1)
# and, that's it, it doesn't take that much care
# whatever

# I hesitate to report metrics, but
# 41ms, 71.79%, 13.9Mb, 73.29%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m + n-2 pick m-1?
        
        # new to python 3.8!
        from math import comb
        return comb(m+n-2,m-1)