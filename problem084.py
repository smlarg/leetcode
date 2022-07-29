heights = [2,1,5,6,2,3]

heights = [6,2,2,2,2,5,2,2,1]




# welp, works, and speed okay enough
# but almost double the median memory, so most people didn't use this many data structures
#1489ms, 51.12%, 48.6Mb, 5.03%
#
# I could clear out the dict as edges go to internal nodes, but it's still possible to be 2/3 full, so I don't think so
#
# Yeah, there's an O(n) time, at most exactly n storage solution:
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/2264465/Easy-python-O(n)-solution-using-stacks
# you go up, keeping a stack of peaks lower than you
# once you find a lower peak, you go back through that list, popping peaks in order of decreasing height
# until you find one shorter than yourself, and calculating heights as you go
# then when you've gone all the way up, you go back down, finding any wide rectangles you missed
# well, anyway,
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        indexedHeights = [(h,i) for i,h in enumerate(heights)]
        indexedHeights.sort(reverse = True)
        
        clusterDict = {}
        
        largestClusterSize = 0
        
        for iH in indexedHeights:
            height = iH[0]
            index = iH[1]
            if (index -1) not in clusterDict:
                myleft = index
            else:
                myleft = clusterDict[index-1][0]
            if (index+1) not in clusterDict:
                myright = index
            else:
                myright = clusterDict[index+1][1]
            
            clusterDict[index] = [myleft,myright]
            
            clusterDict[myleft][1] = myright
            clusterDict[myright][0] = myleft
            
            clusterSize = (myright - myleft +1)*height
            if clusterSize > largestClusterSize:
                largestClusterSize = clusterSize
        
        
        return largestClusterSize

# huh! overwriting heights makes no noteworthy memory change, and greatly slows it down
# The former is probably because...oh, maybe heights doesn't count against me because it's passed in?
# I really don't know why the latter
#2691ms, 5.02%, 47.6Mb, 5.03%
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights = [(h,i) for i,h in enumerate(heights)]
        heights.sort(reverse = True)
        
        clusterDict = {}
        
        largestClusterSize = 0
        
        for iH in heights:
            height = iH[0]
            index = iH[1]
            if (index -1) not in clusterDict:
                myleft = index
            else:
                myleft = clusterDict[index-1][0]
            if (index+1) not in clusterDict:
                myright = index
            else:
                myright = clusterDict[index+1][1]
            
            clusterDict[index] = [myleft,myright]
            
            clusterDict[myleft][1] = myright
            clusterDict[myright][0] = myleft
            
            clusterSize = (myright - myleft +1)*height
            if clusterSize > largestClusterSize:
                largestClusterSize = clusterSize
        
        
        return largestClusterSize

# Didn't submit, would presumably be slower (but easier to follow, I think)
class clusterMember:
    def __init__(self, myleft, myright):
        self.myleft = myleft
        self.myright = myright

class Solution:
    def largestRectangleAreaWithClass(self, heights: List[int]) -> int:
        
        #heights = [0] + heights + [0]
        
        indexedHeights = [(h,i) for i,h in enumerate(heights)]
        indexedHeights.sort(reverse = True)
        #indexedHeights.pop(); indexedHeights.pop();
        
        clusterDict = {}
        
        largestClusterSize = 0
        
        for iH in indexedHeights:
            height = iH[0]
            index = iH[1]
            #if heights[index-1] < height or (index-1) not in clusterDict:
            if (index -1) not in clusterDict:
                myleft = index
            else:
                myleft = clusterDict[index-1].myleft
            if (index+1) not in clusterDict:
                myright = index
            else:
                myright = clusterDict[index+1].myright
            
            clusterDict[index] = clusterMember(myleft,myright)
            
            clusterDict[myleft].myright = myright
            clusterDict[myright].myleft = myleft
            
            clusterSize = (myright - myleft +1)*height
            if clusterSize > largestClusterSize:
                largestClusterSize = clusterSize
        
        
        return largestClusterSize