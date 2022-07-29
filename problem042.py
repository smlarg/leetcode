# hard 4, 40.3%

height = [0,1,0,2,1,0,1,3,2,1,2,1]


# I'm sorry but I'm not sure why this was hard?
# 177ms, 58.97%, no memory of course
# I'm sure there could be a cleverer answer, but, they should have asked that in the question if so
class Solution:
    def trap(self, height: List[int]) -> int:
        # uh, two passes and zero storage is also easy?
        
        maxy, index = 0, -1

        for i, h in enumerate(height):
            if h > maxy:
                maxy = h
                index = i

        total = 0

        left_peak = 0
        for h in height[:index]:
            if h > left_peak:
                left_peak = h
            else:
                total += left_peak-h

        right_peak = 0
        for h in height[:index:-1]:
            if h > right_peak:
                right_peak = h
            else:
                total += right_peak - h
        
        return total


# aha, yes, you can just move in from both sides, then you have an alternating left and right max
#
#I guess I'll just do that?
#
# 155ms, 73.50%
# why do I insist on doing this? Anyway, good.
class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        left_max = height[i]
        right_max = height[j]
        
        total = 0
        
        while i < j:
            if right_max > left_max:
                i += 1
                while height[i] < left_max:
                    total += left_max - height[i]
                    i += 1
                left_max = height[i]
            elif right_max <= left_max:
                j -= 1
                while height[j] < right_max:
                    total += right_max - height[j]
                    j -= 1
                right_max = height[j]
        
        return total
                
                    



class Solution:
    def trap(self, height: List[int]) -> int:
        # welp. This is an O(n) solution, and there's no way to beat O(n)
        # but it's 4*n in time and space
        # since this is trivial otherwise, I'm assuming there's a 2n (or n? I don't think so*) solution, and maybe O(1) space?
        # wish they would say so in the problem descrition though
        #
        # *narrator: there was an n solution
        
        left_max = [0]
        m = 0
        for h in height:
            m = max(m,h)
            left_max.append(m)
        left_max.pop()

        right_max = [0]
        m = 0
        for h in height[::-1]:
            m = max(m,h)
            right_max.append(m)
        right_max.pop()

        right_max.reverse()

        lowest_side = [min(a,b) for a, b in zip(left_max,right_max)]


        s = [max(0,l-h) for l,h in zip(lowest_side,height)]
        
        return sum(s)