# rank just will not change
# 26 medium, 62.4%

intervals = [[15,18],[1,3],[2,6],[8,10],[15,18]]

[[2,3], [15,16], [1,2], [37,39], [14,72]]


# is the trick that there's a way to do it without sorting?
# no, it doesn't seem that way. don't overthing things.
# 156ms, 89.85%, memory as always low variance, but 84.49% so I'll take it
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1],result[-1][1])
            else:
                result.append(interval)
        
        return result