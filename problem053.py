nums = [3,-2,-3,-3,1,3,0]

[-2,1,-3,4,-1,2,1,-5,4]
[1]
[5,4,-1,7,8]
[-1,0,-2]
[3,-2,-3,-3,1,3,0]
[31,-41,59,26,-53,58,97,-93,-23,84]


s = 0
prefix = []
for n in nums:
    s+=n
    prefix.append(s)


class Solution:
    # 753ms, 93.58%
    #
    # you don't need to read any of this, see the solution from the forum.
    #
    # Okay. The idea is, you have to find out how much of the rhs and lhs of the array to drop
    # Or, actually, I guess here it's how much to drop and then how much to include. Right.
    # That's probably why I was so confused.
    # Anyway, the trick is of course what you drop part of what you want to include,
    # and also you can't include nothing
    # so you have to update the drop point *after* you update the include point.
    # Does that make sense?
    # here, another way:
    # you want max(s_j - s_i) where j > i (and s_0 = 0 is included as an option)
    # that's n**2/2 comparisons strictly speaking,
    # but in a single pass it's possible to see which s_i you need to bother considering
    def maxSubArrayOrderN(self, nums: List[int]) -> int:
        lhs = potential_lhs = s = 0
        current_best = nums[0] # any random element in the array is a lower bound
        for n in nums:
            s += n
            # you've found the s described below, drop the whole lhs you found earlier
            # *and* remember the s, but you'll do so in the next step
            if -potential_lhs + s > current_best: lhs = potential_lhs
            # you've found a lhs and an s which is good, so remember it! it's good!
            if -lhs + s > current_best: current_best = -lhs + s
            # if the whole lhs is a loss consider dropping it; you will do so if you find an s which makes it worth your while
            # but *do not* consider it if you've already found an *even worse* lhs
            if s < potential_lhs: potential_lhs = s
        return current_best
    

    # confusing and ineffiecient, and possibly not very correct,
    # but they asked for it
    # 1281ms, 24.68%, not much variance on memory
    #
    # okay, I take that back, this was the much less confusing way to do it
    # it took me forever to get the right way right
    #
    # no. I take back taking it back, see below
    #
    # on the plus side, I found *exactly* this solution in the forums, so it's at least not totally crazy
    def maxSubArrayDivideAndConquer(self, nums: List[int]) -> int:
        
        def maxes(array):
            l = len(array)
            if l == 1:
                return array[0],array[0], array[0], array[0]
            ls, ll, lr, lc = maxes(array[:l//2])
            rs, rl, rr, rc = maxes(array[l//2:])
            
            my_s = ls+rs # you'll need to pass your entire sum up, it will be needed
            
            my_l = max(ll, ls + rl) # to get the best lhs, either use the lhs of the left sub arary
                                    # or suck it up and include *all* of the left array to get to the lhs of the right array
            my_r = max(rr, rs + lr) # same on the other side.
            my_c = max(lc, rc, rl + lr) # the best possible is that of the below arrays, or the possiblity of merging in the middle
            
            return my_s, my_l, my_r, my_c

        return maxes(nums)[-1]
    
    # goddammit.
    def maxSubArrayFromTheForum(self, nums: List[int]) -> int:
        r0 = nums[0]
        m = r0
        
        for n in nums[1:]:
            if r0 > 0:
                r0 += n
            else:
                r0 = n
            m = max(r0,m)
        
        return m