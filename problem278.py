# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # huh. 71ms, which is 5.37% and off the chart slow
    # average is around 40ms
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1) == True:
            return 1
        known_good = 1
        known_bad = n
        while known_bad - known_good > 1:
            if isBadVersion((known_bad + known_good)//2):
                known_bad = (known_bad + known_good)//2
            else:
                known_good = (known_bad + known_good)//2
        return known_bad
    
    # 55ms, 23.13%, so type conversion I guess?
    # still slow though
    def firstBadVersionNoOverflow(self, n: int) -> int:
        known_good = 0
        known_bad = n
        while known_bad - known_good > 1:
            m = known_good + (known_bad - known_good)//2
            if isBadVersion(m):
                known_bad = m
            else:
                known_good = m
        return known_bad
    
    # idea from the metrics page, worth a shot
    # yeah, 50ms, but it doesn't seem right
    def firstBadVersionCheckForHit(self, n: int) -> int:
        known_good = 0
        known_bad = n
        while known_bad - known_good > 1:
            m = known_good + (known_bad - known_good)//2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                else:
                    known_bad = m - 1
            elif isBadVersion(m+1):
                return m+1
            else:
                
                known_good = m+1
        return known_bad