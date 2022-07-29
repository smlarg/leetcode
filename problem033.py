# rank doesn't change
# 22 medium, 59.0%
# 2.0% solved though!
# (I'm not doing 50x what I've invested so far....)

nums = [1,2,3,4,5,6,7,8,9,0]
nums = [9,0,1,2,3,4,5,6,7,8]



from typing import List
# 64ms, 49.29%, I litterally didn't use any memory so I'm not even
# I spent over an hour, good lord maybe two?...yeah almost,
# messing up the <> and or nots
# sigh
#
# I think, the life lesson is, I kept trying to fix my code, iteratively,
# rather than starting again and thinking the whole thing through again from the begining
# when I finally did that I got it
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper_bound = len(nums)-1
        lower_bound = 0
        is_pivoted = nums[lower_bound] > nums[upper_bound]
        
        while is_pivoted:
            if upper_bound < lower_bound: return -1
            search = (upper_bound + lower_bound)//2
            if nums[search] == target: return search
            if not nums[lower_bound] > nums[search]: # now you can check if it's in the lower section, if not it's in the upper section
                if nums[lower_bound] <= target < nums[search]:
                    upper_bound, is_pivoted = search - 1, False
                    continue
                else:
                    lower_bound = search + 1
                    continue
            if not nums[search] > nums[upper_bound]: # and contrariwise, now you can check the upper section
                if nums[search] < target <= nums[upper_bound]:
                    lower_bound, is_pivoted = search + 1, False
                    continue
                else:
                    upper_bound = search - 1
                    continue
            raise Exception("list wasn't sorted")
        
        while upper_bound >= lower_bound:
            search = (upper_bound + lower_bound)//2
            if nums[search] == target: return search
            if target < nums[search]: upper_bound = search - 1; continue
            if target > nums[search]: lower_bound = search + 1; continue
        
        return -1

# just more verbose
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper_bound = len(nums)-1
        lower_bound = 0
        
        is_pivoted = nums[lower_bound] > nums[upper_bound]
        
        while is_pivoted:
            if upper_bound < lower_bound: return -1
            search = (upper_bound + lower_bound)//2
            if nums[search] == target: return search
            upper_pivoted = nums[search] > nums[upper_bound]
            lower_pivoted = nums[lower_bound] > nums[search]
            if not lower_pivoted: # now you can check if it's in the lower section, if not it's in the upper section
                if nums[lower_bound] <= target < nums[search]:
                    upper_bound = search-1
                    is_pivoted = False
                    continue
                else:
                    lower_bound = search + 1
                    continue
            if not upper_pivoted: # and contrariwise, now you can check the upper section
                if nums[search] < target <= nums[upper_bound]:
                    lower_bound = search + 1
                    is_pivoted = False
                    continue
                else:
                    upper_bound = search - 1
                    continue
            raise Exception("list wasn't sorted")
        
        while upper_bound >= lower_bound:
            search = (upper_bound + lower_bound)//2
            if nums[search] == target: return search
            if target < nums[search]:
                upper_bound = search-1
                continue
            if target > nums[search]:
                lower_bound = search+1
                continue
        
        return -1