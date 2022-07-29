# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 109ms, 16.86%, 18.1Mb, 10.35% which fair enough
    def hasCycleDict(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            if head in visited: return True
            else:
                visited[head] = 'anything really'
                head = head.next
        return False
    
    #87ms, 45.02%, 17.9Mb, 19.32%, huh okay
    def hasCycleSet(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited: return True
            else:
                visited.add(head)
                head = head.next
        return False
    
    # 65ms, 79.04%, 17.4Mb, 96.39%
    def hasCycleCheating?(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 131072: return True
            else:
                head.val = 131072
                head = head.next
        return False
    
    # two pointers walking at different speeds seems to be the actual O(1) memory answer