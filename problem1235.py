# 9 hard, 60.7%

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]

startTime = [6,15,7,11,1,3,16,2]
endTime   = [19,18,19,16,10,8,19,8]
profit    = [2,9,1,19,5,7,3,19]

#speed is fine, memory usage is stratospheric
# 712ms, 74.09%, 84.3Mb, 16.01%, correct answer is about 30Mb
#
# aha. you can avoid recursion entirely, by sorting by end instead of by start,
# and then when you condiser a new interval seeing if droping all that confict with it is worth it
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/2262840/Python-or-Binary-Search-%2B-Memo-or-Explained
from typing import List
class Solution:
    def __init__(self):
        self.memo = {}
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # cf https://stackoverflow.com/questions/13668393/python-sorting-two-lists
        
        # overwriting dropped speed to 840ms, 55.16%, and had no effect on memory
        #startTime, endTime, profit = tuple([list(x) for x in zip(*sorted(zip(startTime,endTime,profit),\
        #                                    key=lambda pair: pair[0]))])
        
        startTime2, endTime2, profit2 = tuple([list(x) for x in zip(*sorted(zip(startTime,endTime,profit),\
                                            key=lambda pair: pair[0]))])
        
        self.memo[len(startTime)] = 0
        
        return self.jobScheduling2(startTime2,endTime2,profit2,0)
    
    def jobScheduling2(self, startTime, endTime, profit, i):

        if i in self.memo:
            return self.memo[i]
        
        myEndTime = endTime[i]
        
        # *this* is the one part I thought was sketchy, but it seems to be fine?
        j = i
        while j < len(startTime) and startTime[j]< myEndTime:
            j +=1
        
        result = max( self.jobScheduling2(startTime,endTime,profit,i+1), \
                      self.jobScheduling2(startTime,endTime,profit,j) + profit[i])
        
        self.memo[i] = result
        
        return result

# walking backwards though the list solves the memory, but at the cost of bad speed
# it's just like the encyclopedia says, of course, but, are people bothering to get both? unclear
# 1126ms, 24.08%, 31.9Mb, 45.85%
from typing import List
class Solution:
    def __init__(self):
        self.memo = {}
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # cf https://stackoverflow.com/questions/13668393/python-sorting-two-lists
        startTime2, endTime2, profit2 = tuple([list(x) for x in zip(*sorted(zip(startTime,endTime,profit),\
                                            key=lambda pair: pair[0]))])
        
        self.memo[len(startTime2)] = 0
        
        for i in range(len(startTime2),0,-1):
            devnull = self.jobScheduling2(startTime2,endTime2,profit2,i)
        
        return self.jobScheduling2(startTime2,endTime2,profit2,0)
    
    def jobScheduling2(self, startTime, endTime, profit, i):

        if i in self.memo:
            return self.memo[i]
        
        myEndTime = endTime[i]
        
        j = i
        while j < len(startTime) and startTime[j]< myEndTime:
            j +=1
        
        result = max( self.jobScheduling2(startTime,endTime,profit,i+1), \
                      self.jobScheduling2(startTime,endTime,profit,j) + profit[i])
        
        self.memo[i] = result
        
        return result