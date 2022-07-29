# rank doesn't change
# 23 medium, 59.9%

# cf. problem 322, https://leetcode.com/problems/coin-change/

# there *should* be a way to do this with list comprehesion instead of nested for loops
# but wow does it get crazy quickly, see below
# I certainly couldn't figure it out, and I'm not totally sure I should
#
# oh.
# maybe if I use a .append() instead of a +, inside of the list comprehesion somehow?
# no, seems as bad as anything


# 104ms, 69.23%, memory bad rank as expceted (though only like 10% more than the median)
# I'm just going to leave the memory, at no level does it actually matter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we can save space by making the array only as long as the largest number in candidates
        # and working modulo that number
        # let me try this first though
        
        combs = [ [[]] ]
        
        for i in range(1,target+1):
            c = []
            for num in candidates:
                if num <= i:
                    for comb in combs[i-num]:
                        if comb == [] or num >= comb[-1]:
                            c.append(comb + [num])
            combs.append(c)
        
        return combs[target]



nums = [1,2]
combs[0] = [ [] ]
combs[1] = [ [1] ]
combs[2] = [ [1,1], [2] ]
combs[3] = [ [1,1,1], [1,2] ]
combs[4] = [ [1,1,2], [2,2],[1,1,1,1],[1,2,1] ]# ah no okay

[[x + [num] for x in combs[i-num] if ( x ==[] or x[-1]<= num)] for num in candidates if num <= i]

test = [ [1,1], [2] ]
i = 4
num = 2
[x + [num] for x in combs[i-num] if ( x ==[] or x[-1]<= num)][0]


c = []
i = 1
for num in candidates:
    if num <= i:
        for comb in combs[i-num]:
            if comb == [] or num >= comb[-1]:
                c.append(comb + [num])

[[x.append(num) for x in combs[i-num] if ( x ==[] or x[-1]<= num)] for num in candidates if num <= i]
# nope, it's a bunch of None's, which is interesting, but

[].append('anything') # returns None, so that's probably the root of the issue
c.f.
x = []; x.append(1); print(x)
vs.
x = [].append(1); print(x)
