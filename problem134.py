# rank changed at least though.
# ...to 566,420
# guess I'm well into the long tail then
# stats are 26,46,10

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]

gas  = [0,0,52,7,0,0, 2,0,8,0]
cost = [5,5,17,8,1,1,32,0,0,0]


# bad stats! including memory!
# 925ms, 57.43%, 700 is correct
# 21.5Mb, 5.84%!!!! Correct is 19.5. What?! There's one local variable! I didn't even store len(list)!

# I looked at 700ms solution, it starts with if `sum(gas)<sum(cost)`
# that's one if not two extra passes! that can't be faster!!!
# I'm so annoyed
# 
# okay, well, it *can* be faster, if you hit that so often the overhead of the if statement matters more than a factor of 2
# maybe? who knows. doubtful though, and silly
# so I'm still quite annoyed

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        lowestTank = 0
        gas[0] -= cost[0]
        
        for i in range(1, len(gas)):
            gas[i] += gas[i-1] - cost[i]
            if gas[i] < gas[lowestTank]:
                lowestTank = i
        
        if gas[-1] < 0: return -1
        
        return (lowestTank+1)%len(gas)

# oh thank goodness this is slower
# and 100kb less memory, but at least not much less
class Solution:
    def canCompleteCircuitFuelList(self, gas: List[int], cost: List[int]) -> int:
        # this is silly
        l = len(gas)
        
        lowestTank = 0
        tank = [0 for _ in range(l)]
        tank[0] = gas[0] - cost[0]
        
        for i in range(1, l):
            tank[i] = tank[i-1] + gas[i] - cost[i]
            if tank[i] < tank[lowestTank]:
                lowestTank = i
        
        if tank[-1] < 0: return -1
        
        return (lowestTank+1)%l