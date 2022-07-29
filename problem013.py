# 61ms, 74.67%, no variance in memory but I do feel bad keeping that whole array till the end

class Solution:
    def romanToInt(self, s: str) -> int:
        # c.f. https://projecteuler.net/problem=89
        # I feel like I shouldn't count it, but I mean, I did write the solution myself
        r2a = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        a = []
        for c in s:
            a.append(r2a[c])
            # only ever write IV, never bother with IIV instead of III, so only need to check one previous
            # so the need for an arary at all is questionable
        for i in range(len(a)-1):
            if a[i+1] > a[i]:
                a[i]*=-1
        return sum(a)