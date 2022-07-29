# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 57ms, 22.66%, let's see here...
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        advance = False
        while head:
            head = head.next
            if advance:
                result=result.next
            advance = not advance
        return result

# goddammit, I looked too soon
# inspired by the metrics page
# HAA! 56ms
# yeah, so, it takes up just as much time to look up head.next twice as it does to advance one at a time, makes sense
# the metrics are all system flutter. Forget about it, it's Leet Town.
#
# (This is kind of cleaner code though, so that's fair.)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        while head and head.next:
            result = result.next
            head = head.next.next
        return result