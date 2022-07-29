# rank doesn't change
# 24 medium, 60.8%


# I feel a litle bad, but also, no this is the answer
# metrics don't matter
# okay I guess they do, 69ms
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # I mean
        from itertools import permutations
        return [_ for _ in permutations(nums)]

# dammit. why can't I stop?
# ah, great, 84ms, makes sense
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for num in nums:
            bums = nums.copy()
            bums.remove(num)
            sub_perms = self.permute(bums)
            for sub_perm in sub_perms:
                result.append([num] + sub_perm)
        return result
        
        