# submitted
# and, yes, in the bottom third of speed
# so, maybe try a heap?

#yes, heap is in the top quarter for speed (though it's only a 30% speedup)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        
        indexed = []
        for point in points:
            indexed.append((point[0]**2 + point[1]**2,point))
        
        heapq.heapify(indexed)
        
        # this is slower *and* has more memory than constructing the list in a for loop???
        # I don't know about this
        #return [heapq.heappop(indexed)[1] for _ in range(k)]
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(indexed)[1])
        return result


    def kClosest_regular_sort(self, points: List[List[int]], k: int) -> List[List[int]]:

        # this takes n log(n) time, for the sort
        # techinterviewhandbook.org points out that a heap is n log(k) time
        # *exhale*
        # fine, yes
        # the problem implied k was order n, but...fine yes
        indexed = []
        for point in points:
            indexed.append((point[0]**2 + point[1]**2,point))
        indexed.sort()
        return [b for a,b in indexed[:k]]
