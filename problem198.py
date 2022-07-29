# 27ms, 98.35%, that's the ticket!
# 13.9Mb, 65.75%, but pretty hard to use less memory!


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0: return 0
        if l == 1: return nums[0]
        
        # obvious way:
        #memo = [0 for _ in range(l)]
        #memo[-1] = nums[-1]
        #memo[-2] = max(nums[-2], nums[-1])
        
        # if you're willing to brave evens and odds:
        memo = [0,0]
        memo[1] = nums[-1]
        memo[0] = max(nums[-2], nums[-1])
        
        
        # wait. why did I go backwards? The problem is perfectly symmetric.
        # oh well whatever.
        for i in range(-3,-l-1,-1):
            memo[i%2] = max(memo[(i+1)%2], memo[i%2] + nums[i])

        #return memo[i%2]
        # runtime error, i undefined, wtf!
        # (but only when submitted? extra odd)
        return memo[l%2]