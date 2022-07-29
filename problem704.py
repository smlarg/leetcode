from typing import List


nums, target = [-1,0,3,5,9,12], 13


class Solution:
    #470ms, 13.13%
    def searchNaive(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        diff = 1
        while diff > 0:
            diff = upper-lower
            offset = diff//2
            i = lower + offset
            n = nums[i]
            if n == target:
                return i
            elif n<target:
                lower = i+1
            else:
                upper = i-1
        
        return -1


    # 363ms, 45.37%
    def searchEarlyStopping(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        diff = 1
        if target < nums[lower]:
            return -1
        if target > nums[upper]:
            return -1
        while diff > 0:
            diff = upper-lower
            offset = diff//2
            i = lower + offset
            n = nums[i]
            if n == target:
                return i
            elif n<target:
                lower = i+1
                if target < nums[lower]:
                    return -1
            else:
                upper = i-1
                if target > nums[upper]:
                    return -1
        
        return -1
    
    # 272ms, 78.01%
    def searchFewerVariables(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        if target < nums[lower]:
            return -1
        if target > nums[upper]:
            return -1
        while upper > lower:
            i = (upper + lower)//2
            n = nums[i]
            if n == target:
                return i
            elif n<target:
                lower = i+1
                if target < nums[lower]:
                    return -1
            else:
                upper = i-1
                if target > nums[upper]:
                    return -1
        
        if nums[lower] == target:
            return lower
        
        return -1

    #515ms, so that local variable was worth it
    def searchFewerStill(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) -1
        if target < nums[lower]:
            return -1
        if target > nums[upper]:
            return -1
        while upper >= lower:
            i = (upper + lower)//2
            if nums[i] == target:
                return i
            elif nums[i]<target:
                lower = i+1
                if target < nums[lower]:
                    return -1
            else:
                upper = i-1
                if target > nums[upper]:
                    return -1
        
        return -1