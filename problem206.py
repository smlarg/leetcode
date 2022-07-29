# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 67ms, 23.79%, memory is fine
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newTail = None
        while head:
            newHead = head.next
            head.next = newTail
            newTail = head
            head = newHead
        
        return newTail

# 25ms, 99.84%
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newTail = None
        while head:
            head.next, head, newTail = newTail, head.next, head
        return newTail

# this can't be what they mean, can it?
# it's a loop implemented as an n-deep call stack, there's no way that's a good idea
# in the forum, there are ways to do it without a helper function, that is more interesting
# I think I'm okay though
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHeadAndTail(head)[1]
    def reverseListHeadAndTail(self,head):
        if not head.next:
            return head, head
        newTail, newHead = self.reverseListHeadAndTail(head.next)
        newTail.next = head
        head.next = None
        return head, newHead