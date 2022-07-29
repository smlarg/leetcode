# 5 hard, 46.1%

# 898ms, 42.65%, that's fine, 35.7Mb, 89.10%
class MedianFinder:

    def __init__(self):
        import heapq
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap == []:
            self.minheap.append(num)
            return
        if num > self.minheap[0]:
            heapq.heappush(self.minheap,num)
            if len(self.minheap) > len(self.maxheap) + 1:
                heapq.heappush(self.maxheap,heapq.heappop(self.minheap)*(-1))
            return
        else:
            heapq.heappush(self.maxheap,(-1)*num)
            if len(self.maxheap) > len(self.minheap) + 1:
                heapq.heappush(self.minheap,heapq.heappop(self.maxheap)*(-1))
    def findMedian(self) -> float:
        if self.minheap == []:
            return None
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]*1.0
        elif len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]*(-1.0)
        else:
            return (self.minheap[0] - self.maxheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()