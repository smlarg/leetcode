#submitted

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        num_zeros = 0
        num_twos = 0
        num_ones = 0 #not, of course, needed. But if there's more than 3 categories...
        i = 0
        while i + num_twos < l:
            if nums[i] == 2:
                nums[i] = nums[-1-num_twos]
                nums[-1-num_twos] = 2
                num_twos += 1
            elif nums[i] == 0:
                temp = nums[num_zeros]
                nums[num_zeros] = 0
                nums[i] = temp
                num_zeros += 1
                i += 1
            elif nums[i] == 1:
                # you just leave ones in the middle, and move everything around them
                num_ones += 1
                i+=1
        
        if False:
        # two-pass, and also, really, cheating
        # but, I mean, why not
            t = [0,0,0]
            for n in nums:
                t[n]+=1
            for i in len(nums):
                if i< t[0]:
                    nums[i] = 0
                    continue
                if i < t[0] + t[1]:
                    nums[i] = 1
                    continue
                nums[i] = 2