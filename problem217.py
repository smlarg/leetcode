# uh, ignore everyhting I said below, because its 929ms, 8.02%
# so this is not a good solution. hmm.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # O(n) worst case and expected case (O(1) best fwiw), which is the best I'm pretty sure
        # however O(n) space, which may easily not be the best
        # but they didn't ask for anything better
        #
        # no, I think it has to be O(n) space for O(n) time
        # you can certainly do O(1) space with O(n lgn) time, but why would you?
        
        s = set()
        for n in nums:
            if n in s: return True
            s.add(n)
        return False
        
        #as one line, but O(n) time always
        return len(set(nums)) != len(nums)


# Faster! 770ms, 27.16%
# uh, ey ey ey
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# No, it's all all all systems flutter. It's frustrating,honestly, since they ask about complexity but I guess never test for it.