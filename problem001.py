#submitted

from typing import List

class Solution:   
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mr_hash = {}
        for i, n in enumerate(nums):
            # if there are two keys with the same n, only the last one is stored, and...
            mr_hash[n] = i
        for i, n in enumerate(nums):
            # ...you'll get to the first one first here, so it works out
            # it feels like a hack, but the problem description is very specific about clean input data
            if (target - n) in mr_hash:
                if not i == mr_hash[target-n]:
                    return [i, mr_hash[target-n]]
                    