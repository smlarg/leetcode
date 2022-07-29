#Rank 1,029,876
# 14 medium, 49.3%

nums = [-1,0,1,2,-1,-4]

nums = [-4,-1,-1,0,1,2]

nums = [-12,-5,-4,-3,-3,-1,-1,-1,-1,0,0,1,2,2,2,3,7,9,15]



# 7838ms, 5.08%, and about 8 times the median
# so there is an n solution....
#
# oh thank all that is holy,
# https://en.wikipedia.org/wiki/3SUM
# it's at best known to be n**2
# so why is my solution so slow then? well that's still a mystery
# ah. It's quicker with a sort than a dict? Hmm, why? okay, let me try
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #well, an n**2 solution is a hash table
        
        places = {}
        for i,n in enumerate(nums):
            places[n] = i

        result = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                goal = 0 - nums[i] - nums[j]
                k = places.get(goal,0)
                if k > j:
                    result.add( tuple(sorted( [nums[i],nums[j],nums[k]] )) )
        
        return [ list(t) for t in result ]


# okay.
# 1669ms, 38.55%
# at the top end of the main gaussian (and it's not gaussian, it's poisson), but in it, so
class Solution:
    def threeSumWithSort(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]: continue
            j, k = i+1, len(nums)-1
            while j != k :
                if j < k and nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                if j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j < k and nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j +=1
                    while j < k and nums[j] == nums[k-1]:
                        k -=1
                    if j < k: j +=1
            
        return result
        # there's no way I got that right
        # oh i did, okay.


#skip repeats?? Still n**2
# 8877 ms, 2.46% !!!!!!!1!11bangbang
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        places = {}
        for i,n in enumerate(nums):
            places[n] = i
            
        result = set()
        
        checked_i = set()
        for i in range(len(nums)):
            if i in checked_i: continue
            checked_i.add(i)
            checked_j = set()
            for j in range(i+1,len(nums)):
                if j in checked_j: continue
                checked_j.add(j)
                goal = 0 - nums[i] - nums[j]
                k = places.get(goal,0)
                if k > j:
                    result.add( tuple(sorted( [nums[i],nums[j],nums[k]] )) )
        
        return [ list(t) for t in result ]