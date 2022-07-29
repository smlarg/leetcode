#submitted

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(1) extra space complexity:
        # looks like it could be refactored
        
        l = len(nums)
        
        result = [1]*(l+1)
        p = 1
        for i,n in zip(range(l),nums):
            p*=n
            result[i+1]=p
        
        p = 1
        i = -1
        for n in nums[::-1]:
            #if abs(i)<len(result):
            if True:
                result[i]= result[i-1]*p
            #else:
            #    result[i] = p
            p *= n
            i -= 1
        
        return result[1:]
        

    def productExceptSelf_oh_n_space(self, nums: List[int]) -> List[int]:

        # O(n) extra space complexity, O(n) time:
        # (could use refactoring for more pythonic list usage I think)
        below = [1]
        p = 1
        for n in nums:
            p*=n
            below.append(p)
        #  0 1 2 3 n
        # [1,1,2,6,24]
        above = [1]
        p = 1
        for n in nums[::-1]:
            p*=n
            above.append(p)
        above.reverse()
        #  1  2  3  n  n+1
        #[24,24,12,4, 1]
        
        answer = [below[i] * above[i+1] for i in range(len(nums)) ]
        return answer


        #refactored:
        below = []
        p = 1
        for n in nums:
            below.append(p)
            p*=n
        above = []
        p = 1
        for n in nums[::-1]:
            above.append(p)
            p*=n
        above.reverse()
        return [ a*b for a,b in zip(below,above)]