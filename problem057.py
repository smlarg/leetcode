# rank = 1,029,876
# finished 24,11,1
# 43.8% medium

intervals, newInterval = [[1,3],[5,7],[9,11],[13,15],[17,19]], [4,9]
intervals, newInterval = [[1,3],[5,7],[9,11],[13,15],[17,19]], [23,45]
intervals, newInterval = [[1,3],[5,7],[9,11],[13,15],[17,19]], [1,45]
intervals, newInterval = [[1,3],[5,7],[9,11],[13,15],[17,19]], [17,25]
intervals, newInterval = [[1,3],[5,7],[9,11],[13,15],[17,19]], [4,9]
intervals, newInterval = [[1,3],[6,9]], [2,5]



# 159ms, 16.65%, low memory variance
#
# Seems deceptively simple, but I found it a nightmare of off-by-one errors
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        lower_insert = self.find_interval(intervals,newInterval[0])
        upper_insert = self.find_interval(intervals,newInterval[1])

        # 0 or 1, don't keep any, 2 or 3 keep one, etc.
        # :0 means none, :1 means keep first one, :2 means keep first two
        keep_lower_intervals = lower_insert//2

        # 0 keep all, 1 or 2 skip one, 3 or 4 skip two
        # 0: means keep all, 1: means skip one, 2: means skip two
        keep_upper_intervals = (upper_insert+1)//2

        insert_interval = [0,0]

        if not lower_insert%2: insert_interval[0] = newInterval[0]
        else: insert_interval[0] = intervals[keep_lower_intervals][0]

        if not upper_insert%2: insert_interval[1] = newInterval[1]
        else: insert_interval[1] = intervals[keep_upper_intervals-1][1]

        return intervals[:keep_lower_intervals] + [insert_interval] + intervals[keep_upper_intervals:]


    def find_interval(self, intervals, num):
        # returns 0 for below bottom interval
        # 2n+ 1 for in interval n
        # 2n+ 2 for just above interval n
        
        # I cannot tell you what a pain this was to debug
        
        lower_counter, upper_counter  = 0, 2*len(intervals)
        
        while lower_counter != upper_counter:
            check = ((lower_counter + upper_counter)//2 - 1)//2
            if intervals[check][0] <= num <= intervals[check][1]: return 2*check+1
            if intervals[check][1] < num: lower_counter = check*2 + 2
            if num < intervals[check][0]: upper_counter = check*2
        return upper_counter


# uh, in retrospect, going though the list and building the new list with comparisons probably would have been a lot easier
# I wanted to use a binary search, but you have to build a new list anyway, so you're pretty much stuck with O(n)....
#
# there *are* a few cases where you don't have to build a new list at all, and binary search+checking for that could save a lot of time
# but the test logic is a little convoluted, and I have no data how often such a situation will occur, so I say not worth it
