
# was very confusing and took a lot of writting out exactly what indexies I wanted
# but it worked on first sumbimition (not without testing though of course)

# 55ms, 70.68%
# okay this time no mystery memory increase (unlike 134) so fine cool whatever

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start from the back and move down
        # find the first place the array isn't sorted in reverse order
        # this is j
        # go back up, find the smallest number greater than it; swap j with it
        # array[j+1:l] is now in reverse sorted order and should be sorted
        # so swap all items
        
        # if you don't find anything to swap, reverse the whole array
        
        
        l = len(nums)
        k = -1
        for i in range(l-2,-1,-1):
            if nums[i] < nums[i+1]:
                k = i
                swapLast = True # these monitors always feel graceless
                for j in range(i + 2, l):
                    if nums[j] <= nums[i]:
                        nums[j-1], nums[i] = nums[i], nums[j-1]
                        swapLast = False
                        break
                if swapLast:
                    nums[l-1], nums[i] = nums[i], nums[l-1]
                break
                
        # this was very hard to get just right!
        for i in range(1,(l-k+1)//2):
            nums[k+i], nums[-i] = nums[-i], nums[k+i]
        
        