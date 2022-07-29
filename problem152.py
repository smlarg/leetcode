[2,3,-2,4]
[-2,0,-1]
[-1,0,-1,-2,-3,-5,-1,9]
[-5,0,-3,0,-1,0,-10,0,0]
[0,2,-1,4,-1,4,-1,8,0]
[0,-1,2,-1,4,-1,8,0]
[-2,-2,2,-2,2]


#97ms, 82.06%, so fine whatever
# there's a few obvious fix-ups (final elif's, other if's in different order), but no it's fine
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialization cases:
        # any number > 0: at least that number
        # single negative numbers seperated by zeros: 0
        # exactly one negative number: that number
        # two negative numbers: their product
        
        l = len(nums)
        
        if l == 1 : return nums[0]
        
        negativeTail = 0
        subProduct = 1
        
        # awkward bootstrap into having maxSoFar meaningfully initiated
        if nums[0] > 0:
            subProduct = nums[0]
            maxSoFar = subProduct
            i = 1
        elif nums[0] == 0:
            maxSoFar = 0
            i = 1
        elif nums[0] < 0:
            if nums[1] < 0:
                subProduct = nums[1]
                maxSoFar = nums[0]*nums[1]
                negativeTail = nums[0]
                i = 2
            elif nums[1] == 0:
                maxSoFar = 0
                i = 2
            else:
                subProduct = nums[1]
                maxSoFar = subProduct
                negativeTail = nums[0]
                i = 2
        
        while i < l:
            if nums[i] == 0:
                    negativeTail = 0
                    subProduct = 1
                    while i < l and nums[i] == 0:
                        i += 1
                    if i == l: break
            if nums[i] > 0:
                subProduct *= nums[i]
                if subProduct > maxSoFar:
                    maxSoFar = subProduct
                elif subProduct < 0:
                    if subProduct*negativeTail > maxSoFar:
                        maxSoFar = subProduct*negativeTail
            elif nums[i] < 0:
                if negativeTail == 0:
                    negativeTail = subProduct*nums[i]
                    subProduct = 1
                else:
                    subProduct *= nums[i]
                    if subProduct > maxSoFar:
                        maxSoFar = subProduct
                    elif subProduct < 0:
                        if subProduct*negativeTail > maxSoFar:
                            maxSoFar = subProduct*negativeTail
                
            i+=1
        
        return maxSoFar