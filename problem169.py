[3,2,3]
[2,2,1,1,1,2,2]
[0,1,2,3,4,5,6,7,7,7,7,7,7,7,7]
[0,7,1,2,3,4,5,6,7,7,7,7,7,7,7]
[0,7,1,7,2,7,3,7,4,7,5,7,6,7,7]
[0,7,1,7,2,7,3,7,4,7,5,7,6,7,7]
[6,6,7,7,6,6,7,7,6,6,7,7,6,7,7]
[7,7,7,6,6,6,6,6,7]
[0,0,1]
[0,1,0]
[1,0,0]




# O(n) time with a dict, I assume?


#273ms, 55.63%
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # fwiw, this finds the only candidate for maj
        # a second pass to confirm would be required without the guarentee it exists
        maj = None
        count_maj = 0
        size = 0
        for n in nums:
            size += 1
            if maj == None:
                maj = n
            if n == maj:
                count_maj += 1
            elif size // count_maj >= 2:
                size = 0
                maj = None
                count_maj = 0

        return maj

#350ms, 9.71%, so that sucks. I don't really believe it's slower, but I guess it's not faster
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count_maj = 0
        left = 0
        right = len(nums)
        for n in nums:
            left += 1
            right -=1
            if maj == None: maj = n
            if n == maj:
                count_maj += 1
                if (right+left)//count_maj < 2: return maj
            elif left // count_maj > 1:
                left = 0
                maj = None
                count_maj = 0

        return maj

# 259ms, 44.84%, mrr
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, count_maj, left = None, 0, 0
        rightAndLeft = len(nums)
        for n in nums:
            left += 1
            if maj == None: maj = n
            if n == maj:
                count_maj += 1
                if rightAndLeft//count_maj < 2: return maj
            elif left // count_maj > 1:
                rightAndLeft -= left
                maj, count_maj, left = None, 0, 0
        
        return maj

# improvement (? no early stopping, just fewer vars) influenced by the forums
# HA! NO! Somewhat cheating to run it, but I had to know, and
# 293ms
# (The fewer vars is clearer thinking though)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        count = 1
        for n in nums[1:]:
            if count ==0:
                maj = n
                count = 0
            if n == maj:
                count+=1
            else:
                count-=1
        
        return maj



# wtgf?
# this is an answer from the faster gaussian (179ms):
class Solution:
    ####NOT MINE!!!!!
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n % 2 == 0:
            return nums[int(n/2)]
        else:
            return nums[int((n-1)/2)]
    ####NOT MINE!!!
# it's not even fucuking right (even w/o integer division, there's no else statement necessary)!!!

# okay let me try mine then, fine fuck it
#...
# nope, 307ms, as it should be
# (i mean, it shoud be slower than all of the above really; but at least it's not faster)
class Solution:
    # O(1) space, but nlgn time
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
