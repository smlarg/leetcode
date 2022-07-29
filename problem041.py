# submitted

from typing import List, Set, Dict, Tuple, Optional

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # okay, let's see
        # in O(n) at absolute worst you can find len(nums)
        # any number > len(n) is irrelevent and can be done with as you please
        # same, of course, with num < 1
        #
        # let's just assume we have len(nums), I don't even know how to not in python
        
        l = len(nums)
        for i in range(l):
            # this is only necessary to remove the -1's,
            # but I'm pretty sure that's enough that it can't be simplified
            if nums[i] < 1 or nums[i] > l:
                nums[i] = 0
        
        
        for i in range(l):
            if nums[i] == -1:
                continue
            temp = nums[i]
            while (temp > 0):
                temp2 = nums[temp-1]
                nums[temp-1] = -1
                temp = temp2
        
        for i in range(l):
            if nums[i] != -1:
                return (i+1)
                break
        
        return l+1