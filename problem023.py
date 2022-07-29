# 10 hard, 63.1%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# cool, it's fine, not exceptional but fine
# 185ms, 42.20%, should be about 150, 18.4Mb, 20.00%, lowest is about 17.5Mb
class comparisonWrapper:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    
    def __lt__(self,other):
        return self.val < other.val
    
    def __gt__(self,other):
        return self.val > other.val
    
    def __eq__(self,other):
        return self.val == other.val
    
    def __str__(self):
        return "str CW with val: %i" % (self.val)

    def __repr__(self):
        return "CW with val: %i" %  (self.val)
    
    

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # could add early stopping by tracking if there's only one list left
        import heapq
        
        heapy = []
        rootNode = None
        
        for linkedList in lists:
            if linkedList:
                heapq.heappush(heapy,comparisonWrapper(linkedList.val,linkedList))
        
        if heapy:
            rootNode = heapq.heappop(heapy).node
            if rootNode.next:
                heapq.heappush(heapy, comparisonWrapper(rootNode.next.val, rootNode.next))
        
        currentNode = rootNode
        
        while heapy:
            nodeToAdd = heapq.heappop(heapy).node
            currentNode.next = nodeToAdd
            currentNode = nodeToAdd
            if nodeToAdd.next:
                heapq.heappush(heapy, comparisonWrapper(nodeToAdd.next.val, nodeToAdd.next))
        
        return rootNode