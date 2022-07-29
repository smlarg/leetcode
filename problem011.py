# okay. np.
# 915ms, 70.50%, two peaks at 800ms and 1200ms, can't tell while gausian I'm in
# no variance on memory

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lowerIndex = 0
        upperIndex = len(height) - 1
        
        result = 0
        
        while lowerIndex < upperIndex:
            width = upperIndex - lowerIndex
            mrHeight = min(height[lowerIndex], height[upperIndex])
            area = width*mrHeight
            if area > result: result = area
            if height[lowerIndex] < height[upperIndex]:
                oldHeight = height[lowerIndex]
                while lowerIndex < upperIndex and height[lowerIndex] <= oldHeight:
                    lowerIndex +=1
            else:
                oldHeight = height[upperIndex]
                while lowerIndex < upperIndex and height[upperIndex] <= oldHeight:
                    upperIndex -=1
            
        return result