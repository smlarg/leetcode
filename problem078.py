# medium 32, 66.4%

# interesting, about 20% slower than the median
# maybe doing it by hand is faster? i wouldn't think so though
# 61ms, 28.86%, memory little variance
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        
        result = [[]]
        
        for i in range(1,len(nums)+1):
            result += [list(_) for _ in combinations(nums,i)]
        
        return result

# nope
# 58ms, 36.03%
# we're done here
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        
        for num in nums:
            sub_result = []
            for r in result:
                sub_result.append(r + [num])
            result += sub_result
        
        return result