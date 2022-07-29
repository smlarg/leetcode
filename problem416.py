# 30 med, 65.1%


[1,5,11,5]
[1,2,3,5]
[23,18,5,2,3,6,8,1,2,5,23,18,5,2,3,6,8,1,2,5,11,12,2,2,8,9,13,15,17,12]
[5,3,69,12,68,17,23,18,5,2,3,6,8,1,2,5,11,12,2,2,8,9,13,15,17,12]
[14,9,8,4,3,2]
[1,5,10,6]
[1,2,5]


# Hmm. Takes far too long, but works.
# 6110 ms, 5.47%, a long tail but many answers are 10x faster, and some are 100x!
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)/2
        if int(goal) != goal: return False
        goal = int(goal)

        possibleArray = [[0 for _ in range(goal+1)] for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            possibleArray[i][0] = 1


        for i in range(len(nums)):
            num = nums[i]
            for j in range(goal):
                possibleArray[i+1][j+1] = possibleArray[i][j+1]
                if num > j+1:
                    continue
                possibleArray[i+1][j+1] = possibleArray[i][j+1-num] or possibleArray[i+1][j+1]
            if possibleArray[i][-1]: return True

        return False

# welp, moduloing the array (you only ever need the last row) got me great memory, but only a little speed
# 4496ms, 14.62%, 14.1Mb, 86.64%
class Solution:
    def canPartitionModulo(self, nums: List[int]) -> bool:
        goal = sum(nums)/2
        if int(goal) != goal: return False
        goal = int(goal)

        possibleArray = [[0 for _ in range(goal+1)] for _ in range(2)]

        for i in range(2):
            possibleArray[i][0] = 1


        for i in range(len(nums)):
            num = nums[i]
            for j in range(goal):
                possibleArray[(i+1)%2][j+1] = possibleArray[(i)%2][j+1]
                if num > j+1:
                    continue
                possibleArray[(i+1)%2][j+1] = possibleArray[(i)%2][j+1-num] or possibleArray[(i+1)%2][j+1]
            if possibleArray[(i+1)%2][-1]: return True

        return False

# getting linearly better, but again the goal is 500-50ms. but I think it has to be good enough
# 2751ms, 32.31%
class Solution:
    def canPartitionSort(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        
        goal = sum(nums)/2
        if int(goal) != goal: return False
        goal = int(goal)

        possibleArray = [[0 for _ in range(goal+1)] for _ in range(2)]

        for i in range(2):
            possibleArray[i][0] = 1


        for i in range(len(nums)):
            num = nums[i]
            for j in range(goal):
                possibleArray[(i+1)%2][j+1] = possibleArray[(i)%2][j+1]
                if num > j+1:
                    continue
                possibleArray[(i+1)%2][j+1] = possibleArray[(i)%2][j+1-num] or possibleArray[(i+1)%2][j+1]
            if possibleArray[(i+1)%2][-1]: return True

        return False
        