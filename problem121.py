# 1583 ms, 44.11%
class Solution:
    def maxProfitMinMax(self, prices: List[int]) -> int:
        minnie = prices[0]
        prof = 0
        for n in prices:
            minnie = min(minnie, n)
            prof = max(prof, n-minnie)

        return prof

# slower somehow!, 1629ms
class Solution:
    def maxProfitIf(self, prices: List[int]) -> int:
        minnie = prices[0]
        prof = 0
        for n in prices:
            if n < minnie:
                minnie = n
            else n-minnie > prof:
                prof = n-minnie

        return prof

# and slower still!, 1720ms!!
class Solution:
    def maxProfitElIf(self, prices: List[int]) -> int:
        minnie = prices[0]
        prof = 0
        for n in prices:
            if n < minnie:
                minnie = n
            elif n-minnie > prof:
                prof = n-minnie

        return prof
