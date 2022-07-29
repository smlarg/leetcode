# rank will not change
# 27 medium, 63.1%


# huh. did oddly well in the metrics
# 696ms, 96.25%, well into the right of the poison
# 68.6Mb, 93.86%, in a small bunch near the bottom (the actual bottom is a *tiny* cluster at 61Mb, but still, pretty good)
# oh and I looked at one of the smaller runs, it uses a linear search, so maybe I shouldn't compare myself to that.

class TimeMap:

    def __init__(self):
        self.messages = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.messages:
            self.messages[key][0].append(value)
            self.messages[key][1].append(timestamp)
        else:
            self.messages[key] = ([value],[timestamp]) # does tuple or list make a difference here?
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.messages: return ""
        stamps = self.messages[key][1]
        if timestamp < stamps[0]: return ""
        index = self.findPredecessor(stamps,timestamp)
        return self.messages[key][0][index]
        
    def findPredecessor(self, nums, n):
        # because of the odd logic I use below, 'lower' might be out of the array, so:
        if n > nums[-1]: return len(nums)-1
        
        lower = 0
        upper = len(nums)-1
        while lower <= upper:
            check = (lower + upper)//2
            if nums[check] == n: return check
            if nums[check] > n: upper = check - 1; continue
            if nums[check] < n: lower = check + 1; continue
        
        # maybe? this logic is pretty odd and confusing
        if nums[lower] < n: return lower
        return upper

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)